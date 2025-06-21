import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def extract_article_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract all <p> tags
        paragraphs = soup.find_all('p')
        article_text = ' '.join(p.get_text().strip() for p in paragraphs)
        
        return article_text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def summarize_text(text, max_input_length=20000, max_output_length=500):
    try:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            max_length=max_input_length,
            truncation=True
        )
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=max_output_length,
            min_length=30,
            num_beams=4,
            early_stopping=True
        )
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error during summarization: {str(e)}"

# This part will be replaced by Flask routes
if __name__ == "__main__":
    # Command line testing
    print("Text Summarizer Model Test")
    print("="*30)
    test_url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    print(f"Testing with URL: {test_url}")
    article = extract_article_text(test_url)
    summary = summarize_text(article[:1000])  # Test with first 1000 chars
    print("\nSummary:", summary)