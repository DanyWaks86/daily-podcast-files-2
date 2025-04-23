from flask import Flask, send_from_directory
import os

app = Flask(__name__)
PODCAST_DIR = os.path.join(os.path.dirname(__file__), "podcast")

@app.route("/podcast/<path:filename>")
def serve_podcast_files(filename):
    return send_from_directory(PODCAST_DIR, filename)

@app.route("/")
def home():
    return "🎧 Podcast server is live!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
