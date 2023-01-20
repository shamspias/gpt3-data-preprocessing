import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import json

# Open the PDF file
with open('book.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    # Iterate through each page of the PDF
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()

# Tokenize the text
tokens = word_tokenize(text)

# Remove stop words and punctuation
stop_words = set(stopwords.words('english'))
tokens = [token.lower() for token in tokens if token not in stop_words and token not in string.punctuation]

# Save the preprocessed data as a JSON file
with open('book_data.json', 'w') as json_file:
    json.dump(tokens, json_file)
