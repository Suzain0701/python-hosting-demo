
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Python Website</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: #f3f6fa;
                padding: 60px 20px;
            }
            .card {
                max-width: 600px;
                margin: auto;
                padding: 35px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 15px #00000015;
            }
            h1 { color: #174ea6; }
            a {
                display: inline-block;
                margin: 10px;
                color: white;
                background: #174ea6;
                padding: 12px 20px;
                text-decoration: none;
                border-radius: 6px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>My Python Website</h1>
            <p>Hello! My Flask application is running successfully.</p>
            <p>This website is built using Python.</p>
            <a href="/about">About</a>
            <a href="/health">Health Check</a>
        </div>
    </body>
    </html>
    """


@app.route("/about")
def about():
    return """
    <h1>About This Website</h1>
    <p>This website is built with Python and Flask.</p>
    <a href="/">Back to Home</a>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is running"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )