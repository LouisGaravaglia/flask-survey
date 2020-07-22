from flask import Flask, request, render_template, session, make_response, redirect
from surveys import satisfaction_survey
from random import choice, randint
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 

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
    text = main_question.allow_text
    
    return render_template("question_0.html", question=question, choices=choices, text=text)


@app.route('/questions/0/answer', methods=["POST"])
def answer_0():
    """keeps track of answer to first question"""
    option = request.form["options"]
    text = request.form.get("text", "false")
    answers.append(option)
    if not text == "false":
        answers.append(text)
    
    return redirect("/questions/1")    

# /////////////////////////////////////////////////////// SECOND QUESTION

@app.route('/questions/1')
def question_1():
    """shows second question"""
    main_question = satisfaction_survey.questions[1]
    question = main_question.question
    choices = main_question.choices
    text = main_question.allow_text


    return render_template("question_1.html", question=question, choices=choices, text=text)
    
@app.route('/questions/1/answer', methods=["POST"])
def answer_1():
    """keeps track of answer to second question"""
    option = request.form["options"]
    text = request.form.get("text", "false")
    answers.append(option)
    if not text == "false":
        answers.append(text)
    
    return redirect("/questions/2")    
    


# /////////////////////////////////////////////////////// THIRD QUESTION

@app.route('/questions/2')
def question_2():
    """shows third question"""
    main_question = satisfaction_survey.questions[2]
    question = main_question.question
    choices = main_question.choices
    text = main_question.allow_text


    return render_template("question_2.html", question=question, choices=choices, text=text)
    
@app.route('/questions/2/answer', methods=["POST"])
def answer_2():
    """keeps track of answer to third question"""
    option = request.form["options"]
    text = request.form.get("text", "false")
    answers.append(option)
    if not text == "false":
        answers.append(text)
    
    return redirect("/questions/3")    

# /////////////////////////////////////////////////////// FOURTH QUESTION

@app.route('/questions/3')
def question_3():
    """shows fourth question"""
    main_question = satisfaction_survey.questions[3]
    question = main_question.question
    choices = main_question.choices
    text = main_question.allow_text


    return render_template("question_3.html", question=question, choices=choices, text=text)
    
@app.route('/questions/3/answer', methods=["POST"])
def answer_3():
    """keeps track of answer to third question"""
    option = request.form["options"]
    text = request.form.get("text", "false")
    answers.append(option)
    if not text == "false":
        answers.append(text)
    
    return redirect("/thank_you")

# /////////////////////////////////////////////////////// THANK YOU

@app.route('/thank_you')
def thanks():
    """thanks the user for subming survey"""


    return render_template("thank_you.html", answers=answers)
    

    

