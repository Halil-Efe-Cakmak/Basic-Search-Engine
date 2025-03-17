import os
import json
from tika import parser
import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict

class SearchEngine:
    def __init__(self, docs_folder):
        self.docs_folder = docs_folder
        self.index = defaultdict(list)

    def extract_text(self, file_path):
        """Extract text from a file using Apache Tika"""
        raw = parser.from_file(file_path)
        return raw["content"] if raw["content"] else ""

    def process_text(self, text):
        """Clean and tokenize text"""
        tokens = word_tokenize(text.lower())  # Convert to lowercase and tokenize
        return [word for word in tokens if word.isalnum()]  # Keep only alphanumeric words

    def build_index(self):
        """Extract text from all files, process them, and create an inverted index"""
        for filename in os.listdir(self.docs_folder):
            file_path = os.path.join(self.docs_folder, filename)
            try:
                text = self.extract_text(file_path)
                tokens = self.process_text(text)

                # Index each word with the document it appears in
                for word in set(tokens):
                    self.index[word].append(filename)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

        # Save the index as a JSON file
        with open("index.json", "w") as f:
            json.dump(self.index, f, indent=4)

        print("Indexing completed!")

# Folder containing documents
docs_folder = r"C:\Users\hefec\Desktop\Documents"

# Initialize the search engine and build the index
engine = SearchEngine(docs_folder)
engine.build_index()
