# AI Text Summarizer

This application uses the BART-Large-CNN model to generate concise summaries from web articles or pasted text.

## Features

- Summarize text from a URL
- Summarize directly pasted text
- Clean and responsive web interface

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```

2. Create a virtual environment and activate it:
```
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```
python app.py
```

2. Open your web browser and navigate to: http://127.0.0.1:5000

3. Choose either URL or Text input method:
   - If URL: Paste a valid URL starting with http:// or https://
   - If Text: Paste or type the text you want to summarize

4. Click the "Summarize" button and wait for the result

## Technical Details

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- AI Model: facebook/bart-large-cnn from Hugging Face Transformers
- Text Extraction: BeautifulSoup4

## License

MIT