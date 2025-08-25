import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # This will now correctly fetch the URL you provide
    preview_url = os.environ.get("PREVIEW_URL")
    return f"Hello! My preview URL is: {preview_url}"

if __name__ == "__main__":
    # The PORT is also provided by your platform
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
