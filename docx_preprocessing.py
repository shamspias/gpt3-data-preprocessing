import docx
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import json

# Open the DOCX file
doc = docx.Document('article.docx')
text = ""
# Iterate through each paragraph of the DOCX
for para in doc.paragraphs:
    text += para.text

# Tokenize the text
tokens = word_tokenize(text)

# Remove stop words and punctuation
stop_words = set(stopwords.words('english'))
tokens = [token.lower() for token in tokens if token not in stop_words and token not in string.punctuation]

# Save the preprocessed data as a JSON file
with open('article_data.json', 'w') as json_file:
    json.dump(tokens, json_file)
