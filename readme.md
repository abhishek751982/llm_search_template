# LLM-Based RAG System

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system using Large Language Models (LLMs). The system features:
- Streamlit frontend for user interaction
- Flask backend for processing
- Web scraping capabilities
- LLM integration for answer generation

## Screenshots

### User Interface
| Empty State | With Results |
|-------------|--------------|
| ![Screenshot 2025-04-20 001002](https://github.com/user-attachments/assets/04fa6041-65e6-4310-9aa1-b19b80d0f13b) | ![Screenshot 2025-04-20 001716](https://github.com/user-attachments/assets/a97fff18-a573-41ae-bd8a-91ddccb30ac8) |

### Terminal Views
| Streamlit Server | Flask Backend |
|------------------|---------------|
| ![Screenshot 2025-04-20 001446](https://github.com/user-attachments/assets/708d016a-2e2d-453a-a104-c044bb5d2132) | ![Screenshot 2025-04-20 001532](https://github.com/user-attachments/assets/66c2b61c-644d-47d3-9bf9-f88d464f9573) |

## System Architecture

```mermaid
graph TD
    A[User Query] --> B[Streamlit Frontend]
    B --> C[Flask Backend]
    C --> D[Web Scraping]
    D --> E[Content Processing]
    E --> F[LLM Generation]
    F --> G[Response Display]
```
## Installation Guide
### 1. **Prerequisites**
- Python 3.8+

### 2. **Setup Environment**

```bash
# Clone repository
git clone https://github.com/abhishek751982/llm_search_template
cd llm_search_template

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
### 3. **Configuration**
- Create .env file:
```bash
OPENAI_API_KEY=your_api_key_here
SEARCH_API_KEY=your_search_key
```
4. **Running the System**
```bash
# Terminal 1 - Start Flask backend
cd flask_app
python app.py

# Terminal 2 - Start Streamlit frontend
cd streamlit_app
streamlit run app.py
```
## Usage Instructions
- Access http://localhost:8501 in your browser

- Enter your query in the search box

- Click "Search" button

- View generated results
