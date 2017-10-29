#export FLASK_APP=midterm.py
#python -m flask run

from flask import Flask, request, render_template, make_response
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
import requests
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.debug = True 

@app.route('/')
def hello_world():
	response = make_response('<h1>  This page contains a cookie. There have been 44 presidents of the United States with two main political parties. </h1> <br> <a href = "/parties/democrat" > democrat? </a> <a href = "/parties/republican" > republican? </a>')
	response.set_cookie('president', 'the year')
	return response

class YearForm(FlaskForm):
	radio = RadioField('Select a year:', choices = [('2008', '2008'), ('2012', '2012'), ('2016', '2016')])
	submit = SubmitField('Submit')

@app.route('/year')
def pick_a_year():
	form2 = YearForm()
	return render_template("years.html", form=form2)

@app.route('/candidates' , methods=['GET', 'POST'])
def listofcandidates():
	requests = YearForm(request.form)
	x = requests.radio.data
	print (x)
	return render_template("candidateresponse.html" , x = x)

@app.route('/candidates/<candidateName>')
def candidate(candidateName):
	return (candidateName) + " once ran for president of the United States of America."

@app.route('/party/<partyName>')
def party(partyName):
	return render_template("parties.html", x=partyName)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def servererror(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()