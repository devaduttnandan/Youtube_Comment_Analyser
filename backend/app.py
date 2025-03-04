from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

YOUTUBE_API_KEY = "Enter your Youtube API key here"
MISTRAL_API_KEY = "Enter your Mistral API key here" 
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"  

def get_youtube_comments(video_id):
    """Fetch comments for a given YouTube video ID."""
    url = f"https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "key": YOUTUBE_API_KEY,
        "maxResults": 10
    }
    response = requests.get(url, params=params)
    data = response.json()
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in data.get('items', [])]
    return comments

def analyze_comment(comment):
    """Analyze a comment using Mistral API."""
    prompt = f"""
    Analyze the following comment and classify it as 'negative' or 'neutral'. 
    Also, indicate if it is controversial. Comment: {comment}
    """
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-medium",  
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)
        response.raise_for_status()  
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error calling Mistral API: {str(e)}")
        return "Error: Unable to analyze comment."

@app.route('/analyze', methods=['POST'])
def analyze():
    """Endpoint to analyze YouTube comments."""
    data = request.json
    video_url = data.get("video_url")
    
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
    except Exception:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    comments = get_youtube_comments(video_id)

    analyzed_comments = []
    for comment in comments:
        analysis = analyze_comment(comment)
        analyzed_comments.append({"comment": comment, "analysis": analysis})

    return jsonify(analyzed_comments)

if __name__ == '__main__':
    app.run(debug=True)
