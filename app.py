#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, jsonify
import requests


# Create the application.
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_input', methods=['POST'])
def user_input():
	print request.form
	return redirect('/')

@app.route('/search', methods=['GET'])
def search():
	#Airport API goes here
    s = requests.get("http://terminal2.expedia.com/x/cars/search?pickupdate=2016-03-21T10:00&dropoffdate=2016-03-28T16:30&pickuplocation=SEA&dropofflocation=SEA&sort=price&limit=10&apikey=BQBh6sGziLeQsNQxVjHPlaO08ATfLKn7")
    #Coverts API into JSON and sends it back to the client-side
    return jsonify(s.json())

app.run(debug=True) 
