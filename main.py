from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>Basic Flask Page</title>
    </head>
    <body>
        <h1>Welcome to Flask!</h1>
        <p>This is a basic HTML page served by Flask.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000)
  
