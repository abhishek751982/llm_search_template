import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load API keys from environment
load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def search_articles(query):
    """
    Searches for articles related to the query using Serper API.
    Returns a list of dictionaries containing article URLs and titles.
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    articles = []
    for item in data.get("organic", [])[:3]:  # Get top 3 articles
        articles.append({
            "title": item.get("title"),
            "url": item.get("link")
        })

    return articles


def fetch_article_content(url):
    """
    Fetches the article content, extracting headings and text.
    """
    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, "html.parser")
        elements = soup.find_all(["h1", "h2", "h3", "p"])
        content = "\n".join(elem.get_text() for elem in elements if len(elem.get_text()) > 30)
        return content.strip()
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return ""


def concatenate_content(articles):
    """
    Concatenates the content of the provided articles into a single string.
    """
    full_text = ""
    for article in articles:
        content = fetch_article_content(article["url"])
        if content:
            full_text += f"\n\n### {article['title']}\n{content}"
    return full_text.strip()


def generate_answer(content, query):
    """
    Generates an answer from the concatenated content using OpenAI's GPT model.
    """
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""Use the following information to answer the user's question.

Context:
{content}

Question: {query}

Answer:"""

    payload = {
        "model": "gpt-3.5-turbo",  # Change to gpt-4 if needed
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    try:
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("OpenAI API error:", result)
        return "Sorry, I couldn't generate an answer at this time."
