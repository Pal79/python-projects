from flask import Flask, render_template
import requests

API_ENDPOINT = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
posts = requests.get(API_ENDPOINT).json()
#print(posts)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        all_posts=posts
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)