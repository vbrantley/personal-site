import os
from sys import argv
from flask import Flask, request, make_response, redirect, url_for, session, jsonify
from flask import render_template

app = Flask(__name__, template_folder='templates')

#-------------------------------------------------------------------------------

@app.route('/')
def home():

    html = render_template('home.html')
    response = make_response(html)
    return response

#-------------------------------------------------------------------------------

@app.route('/portfolio')
def portfolio():

    html = render_template('portfolio.html')
    response = make_response(html)
    return response

#-------------------------------------------------------------------------------

@app.route('/picks')
def picks():

    html = render_template('picks.html')
    response = make_response(html)
    return response

#-------------------------------------------------------------------------------

@app.route('/contact')
def contact():

    html = render_template('contact.html')
    response = make_response(html)
    return response

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)
