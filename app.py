from flask import Flask, request, render_template, session, make_response
from surveys import satisfaction_survey
from random import choice, randint


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"



@app.route('/')
def home_page():
    """shows home page"""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template("home.html", title=title, instructions=instructions)