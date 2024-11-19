import PyPDF2
import pytesseract
from PIL import Image
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import requests
from bs4 import BeautifulSoup
# from copyleaks import CopyleaksAPI

# Ensure NLTK data is downloaded
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    return " ".join(word for word in words if word.isalnum() and word not in stop_words)

def extract_text_from_pdf(pdf_file):
    text = ''
    try:
        reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
        return text if text.strip() else "No readable text found in PDF."
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_image(image_file):
    try:
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img)
        return text if text.strip() else "No readable text found in image."
    except Exception as e:
        return f"Error reading image: {str(e)}"


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(input_text):
    # Example stored content to compare against. In a real application, retrieve this from a database.
    stored_content = [
        "This is a sample document stored for comparison.",
        "Another example content that might match the user's input.",
        "Common phrases and information that help measure similarity."
    ]
    
    # Add input text to stored content list
    documents = stored_content + [input_text]

    # Vectorize texts using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Calculate cosine similarity between input and each stored document
    similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]).flatten()
    
    # Find maximum similarity score
    max_similarity = max(similarities)
    
    # Convert to percentage
    plagiarism_percentage = max_similarity * 100
    return plagiarism_percentage



# # Function to scrape text from a URL
def scrape_url(url):
    try:
        # Fetch content from the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content (can adjust selectors based on the website structure)
        paragraphs = soup.find_all('p')
        text_content = ' '.join([para.get_text() for para in paragraphs])
        return text_content
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None

# # Function to check plagiarism using Copyleaks
def check_plagiarism(text_content):
    api_key = 'YOUR_COPYLEAKS_API_KEY'  # Replace with your Copyleaks API key
    email = 'YOUR_EMAIL'  # Your Copyleaks account email

    try:
        # Initialize Copyleaks API client
        api = CopyleaksAPI(api_key, email)
        result = api.scan_text(text_content)

        # Check for plagiarism matches and extract source details
        plagiarism_sources = []
        if result and 'results' in result:
            for match in result['results']:
                source_url = match.get('source', 'Unknown')
                plagiarism_sources.append(source_url)

        return plagiarism_sources
    except Exception as e:
        print(f"Error checking plagiarism: {e}")
        return None
