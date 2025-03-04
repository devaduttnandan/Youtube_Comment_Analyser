This Flask-based web application analyzes YouTube video comments, identifies negative and controversial comments, and summarizes them for further review. The app uses the YouTube Data API to fetch comments and the Mistral AI API (or an alternative NLP provider) to classify and analyze the sentiment of each comment.7

**Features**

Fetches all comments from a YouTube video using the YouTube Data API.
Analyzes each comment for sentiment (negative, neutral, or positive) and controversy level (1–10).
Filters and returns only highly controversial negative comments .
Lightweight and scalable backend built with Flask.

**Prerequisites**
Before running the application, ensure you have the following:

Python 3.8+ : Install Python from python.org .
YouTube Data API Key : Obtain an API key from the Google Cloud Console .
Mistral AI API Key : Sign up for Mistral AI and obtain an API key (or use an alternative provider like Hugging Face or OpenAI).
Dependencies : Install the required libraries using pip.

Output

![image](https://github.com/user-attachments/assets/fa10d072-93a9-4473-abd4-82d0cec239e4)
