from flask import Flask, render_template, request, jsonify
from summarizer import extract_article_text, summarize_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    input_type = data.get('type')
    content = data.get('content')
    
    try:
        if input_type == 'url':
            article = extract_article_text(content)
            if article.startswith("Error"):
                return jsonify({'summary': article})
        else:
            article = content
        
        summary = summarize_text(article)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'summary': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    print("Starting Text Summarizer Web App...")
    print("Loading AI model...")
    # Model loading happens when importing summarizer.py
    print("Model loaded successfully!")
    print("Navigate to http://127.0.0.1:5000 in your web browser")
    app.run(debug=True)