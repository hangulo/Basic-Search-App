__author__ = 'Angulo'

from flask import Flask, render_template, request
from app.forms import ContactForm,SearchForm
from app.search import *

app = Flask(__name__)

app.secret_key = 'hihi123456'

@app.route('/', methods=['GET', 'POST'])
def root():
    form = SearchForm()
    if request.method == 'POST':
        subdomain2 = str(form.subdomain.data)
        print subdomain2 + "!!!!!!!!!!!!!"
        subdomain = "chopperui.loggly.com"
        rsid= initiateSearch(subdomain)
        results_JSON= getSearchResults(rsid, subdomain2)

        events_JSON = results_JSON["events"]
        results_TXT= json.dumps(results_JSON, sort_keys=True,indent=4, separators=(',', ': '))
        events_TXT= json.dumps(events_JSON, sort_keys=True,indent=4, separators=(',', ': '))

        events_num =  str(results_JSON["total_events"])
        page_num = str(results_JSON["page"])
        print "# of events: "+ events_num
        print "Page "+ page_num
        print "############   Just Events: "+ str(results_JSON["events"])

        return render_template('results.html',form=form, x=events_num, y=events_TXT, z=events_num )
    return render_template('index.html', form=form)


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