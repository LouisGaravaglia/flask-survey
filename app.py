from flask import Flask, request, render_template, session, make_response, redirect
from surveys import satisfaction_survey
from random import choice, randint
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"

debug = DebugToolbarExtension(app)

answers = []

# //////////////////////////////////////////////////////// HOME

@app.route('/')
def home_page():
    """shows home page"""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template("home.html", title=title, instructions=instructions)

# /////////////////////////////////////////////////////// FIRST QUESTION

@app.route('/questions/0')
def question_0():
    """shows first question"""
    main_question = satisfaction_survey.questions[0]
    question = main_question.question
    choices = main_question.choices
    
    return render_template("question_0.html", question=question, choices=choices)


@app.route('/questions/0/answer', methods=["POST"])
def answer_0():
    """keeps track of answer to first question"""
    option = request.form["options"]
    answers.append(option)
    
    return redirect("/questions/1")    

# /////////////////////////////////////////////////////// SECOND QUESTION

@app.route('/questions/1')
def question_1():
    """shows second question"""
    main_question = satisfaction_survey.questions[1]
    question = main_question.question
    choices = main_question.choices
    
    return render_template("question_1.html", question=question, choices=choices)
    
@app.route('/questions/1/answer', methods=["POST"])
def answer_1():
    """keeps track of answer to second question"""
    option = request.form["options"]
    answers.append(option)
    
    # return redirect("/")    
    return render_template("answer_1.html", answers=answers)



