import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, dsshhjsjsddzs!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"

    # Get the platform-provided preview URL if available
    preview_url = os.environ.get("URL") or os.environ.get("REPL_URL") or "http://127.0.0.1:{port}/"
    print(f"Preview URL: {preview_url}")

    app.run(host=host, port=port)
    
