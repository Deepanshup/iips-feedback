import os
import smtplib
import datetime as dt
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/register",methods=["POST"])
def register():
    name=request.form.get("name")
    semester=request.form.get("semester")
    email=request.form.get("email")
    feedback = request.form.get("feedback")
    if not name or not semester or not email or not feedback:
        return render_template("failure.html")
    message="You are REGISTERED! on {}".format(str(dt.datetime.now()))
    with open("registered.txt", 'a') as file:
        file.write(name + "," + semester + "," + email + "," + feedback + "\n")
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("deepanshu01pathak@gmail.com",os.getenv("PASSWORD"))
    server.sendmail("deepanshu01pathak@gmail.com",email,message)
    return render_template("success.html")
app.run()
