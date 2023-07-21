import smtplib
from flask import Flask, render_template, request
import requests

OWN_EMAIL = 'vishali86076@gmail.com'
OWN_PASSWORD = 'pythsxypokfhvzsp'

app = Flask(__name__)

"""
Delete previous code:
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"
"""

# SOLUTION to Challenge:
@app.route("/contact", methods=["POST", 'GET'])
def contact():

    if request.method == 'POST':
        method = request.method
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html',method= method)

    method = 'GET'
    return  render_template('contact.html',method=method)



def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

# Code from Day 59 below:
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/78fe818106f262159f2a").json()

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")




@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)








if __name__ == "__main__":
    app.run(debug=True)