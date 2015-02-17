__author__ = 'Angulo'

from flask import Flask, render_template, request
from app.forms import ContactForm
from app.search import *

app = Flask(__name__)

app.secret_key = 'hihi123456'

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        results= getSearchResults(initiateSearch())
        print "Results here: "+ results
        return render_template('results.html', success=True, x=results, y=2)
    return render_template('index.html')


@app.route('/contact',  methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        results= getSearchResults(initiateSearch())
        print "Results here: "+ str(results)
        return render_template('contact.html', success=True, x=results, y=2)

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)