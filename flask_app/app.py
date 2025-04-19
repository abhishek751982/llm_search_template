from flask import Flask, request, jsonify
import os
from utils import search_articles, concatenate_content, generate_answer

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer and intermediate steps.
    """
    try:
        data = request.get_json()
        user_query = data.get('query')
        print("Received query:", user_query)

        # Step 1: Search and scrape articles
        print("Step 1: Searching articles...")
        articles = search_articles(user_query)
        print("Found articles:", articles)

        # Step 2: Concatenate content from the scraped articles
        print("Step 2: Concatenating content...")
        content = concatenate_content(articles)
        print("Concatenated content (preview):", content[:500])  # Show a snippet

        # Step 3: Generate answer using LLM
        print("Step 3: Generating answer...")
        answer = generate_answer(content, user_query)
        print("Generated answer:", answer)

        # Return the answer and intermediate results
        return jsonify({
            "answer": answer,
            "query": user_query,
            "num_articles": len(articles) if articles else 0,
            "article_titles": [a.get('title', 'No Title') for a in articles] if articles else [],
            "content_snippet": content[:1000]  # To avoid overwhelming the response
        })

    except Exception as e:
        print("Error occurred:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
