__author__ = 'Angulo_Hector'

from flask import Flask, render_template, request
from app.forms import *
from app.search import *

app = Flask(__name__)

app.secret_key = 'hihi1234567'

@app.route('/', methods=['GET', 'POST'])
def root():
    form = SearchForm()
    if request.method == 'POST':
        # Get the user's inputs
        subdomain = str(form.subdomain.data)
        searchFrom = str(form.searchFrom.data)
        searchTo = str(form.searchTo.data)
        query = str(form.query.data)
        size = str(form.size.data)
        user = str(form.user.data)
        password = str(form.password.data)

        ## Begin the Search Query
        rsid= initiateSearch(subdomain,searchFrom,searchTo,query,size,user,password)
        results_JSON= getSearchResults(rsid, subdomain, user,password)
        facets_JSON= getFields(subdomain,searchFrom,searchTo,query, user, password)

        events_JSON = results_JSON["events"]
        results_TXT= json.dumps(results_JSON, sort_keys=True,indent=4, separators=(',', ': '))
        events_TXT= json.dumps(events_JSON, sort_keys=True,indent=4, separators=(',', ': '))
        facets_TXT= json.dumps(facets_JSON, sort_keys=True,indent=4, separators=(',', ': '))
        events_num =  str(results_JSON["total_events"])

        #print json.dumps(results_JSON, sort_keys=True,indent=4, separators=(',', ': '))
        print json.dumps(results_JSON, sort_keys=True,indent=4, separators=(',', ': '))

        #print "------"
        #print json.dumps(events_JSON[0]["event"], sort_keys=True,indent=4, separators=(',', ': '))

        return render_template('results.html',form=form, num_events=events_num, events_txt=events_TXT,
                               facets_TXT=facets_TXT, events_JSON=events_JSON)
    return render_template('index.html', form=form)

@app.route('/analyze',  methods=['GET', 'POST'])
def analyze():
    form = AnalyzeForm()

    if request.method == 'POST':

        print "Pressed Analyze Button"
        return render_template('analyze.html', form=form, success=True)

    elif request.method == 'GET':
        return render_template('analyze.html', form=form)

@app.route('/angular',  methods=['GET', 'POST'])
def angular():
    return render_template('angular.html')


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