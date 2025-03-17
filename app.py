from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Homepage (HTML interface)
@app.route('/')
def home():
    return render_template("index.html")

# Function to load index data from a JSON file
def load_index():
    with open("index.json", "r", encoding="utf-8") as f:
        return json.load(f)

# 🔍 Search function
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")  # Get the user's input word
    if not query:
        return jsonify({"error": "Please enter a word!"}), 400

    index = load_index()  # Load the index file
    query = query.lower()  # Convert to lowercase
    results = index.get(query, [])  # Retrieve files containing the word

    return jsonify({"query": query, "results": results})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)