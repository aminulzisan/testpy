import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    # Build preview URL like Express.js: ${req.protocol}://${req.get('host')}/
    preview_url = request.url_root
    print(f"Preview URL: {preview_url}")  # prints on each request
    return f"Hello, dsshhjsjsddzs!<br>Preview URL: {preview_url}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
