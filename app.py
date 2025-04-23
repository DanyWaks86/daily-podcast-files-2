from flask import Flask, send_from_directory
import os

app = Flask(__name__)
PODCAST_DIR = os.path.join(os.getcwd(), "podcast")

@app.route("/podcast/<path:filename>")
def serve_podcast_files(filename):
    return send_from_directory(PODCAST_DIR, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
