from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend from different port

# Load zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news_text = data.get('news', '')

    labels = ["real", "fake"]
    result = classifier(news_text, candidate_labels=labels)

    return jsonify({
        "news": news_text,
        "label": result['labels'][0],
        "score": float(result['scores'][0])
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
