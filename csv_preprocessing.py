import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import json

# Read the CSV file
df = pd.read_csv('articles.csv')
text = " ".join(review for review in df.text)

# Tokenize the text
tokens = word_tokenize(text)

# Remove stop words and punctuation
stop_words = set(stopwords.words('english'))
tokens = [token.lower() for token in tokens if token not in stop_words and token not in string.punctuation]

# Save the preprocessed data as a JSON file
with open('article_data.json', 'w') as json_file:
    json.dump(tokens, json_file)
