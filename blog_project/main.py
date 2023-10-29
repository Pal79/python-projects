from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = "pal.daniel.79@gmail.com"
OWN_PASSWORD = "OWN_PASSWORD"

API_ENDPOINT = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
posts = requests.get(API_ENDPOINT).json()
#print(posts)
PORT = 587

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

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        email_send(
            data["name"],
            data["email"],
            data["phone"],
            data["message"]
        )
        return render_template(
            "contact.html",
            msg_sent=True
        )
    return render_template(
        "contact.html",
        msg_sent=False
    )

@app.route("/post/<int:id>")
def post(id):
    requested_post = None
    for post in posts:
        if post["id"] == id:
            requested_post = post
    return render_template(
        "post.html",
        post=requested_post
    )

def email_send(name,email,phone,message):
    email_message = f"Subject: New Message\n\n" \
                    f"Name: {name}\n" \
                    f"Email: {email}\n" \
                    f"Phone: {phone}\n" \
                    f"Message:\n" \
                    f"{message}"
    enc_msg = email_message.encode("UTF-8")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=OWN_EMAIL,
            password=OWN_PASSWORD
        )
        connection.sendmail(
            from_addr=OWN_EMAIL,
            to_addrs=OWN_EMAIL,
            msg=enc_msg
        )

if __name__ == "__main__":
    app.run(debug=True)