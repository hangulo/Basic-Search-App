__author__ = 'Angulo'

import requests, json

#accountFqdn= "chopperui.loggly.com"
query= "*0"
searchFrom= "-1m"
searchTo= "now"


def initiateSearch(accountFqdn):

    search_url = ("https://" + accountFqdn + "/apiv2/search?q=" + query + "&from=" +
                  str(searchFrom) + "&until=" + str(searchTo) + "&order=asc&size=1")

    #print "Search URL: " + search_url

    r = requests.get(search_url, auth=('hector', 'hector'))
    #print json.dumps(r.json(), sort_keys=True,
      #  indent=4, separators=(',', ': '))

    try:
        rsid = r.json()['rsid']['id']
        #print "rsid: " + str(rsid)

    except ValueError:
        print("Error obtaining data")
        return -1

    return rsid

def getSearchResults(rsid, accountFqdn):
    search_url = ("https://" + accountFqdn + "/apiv2/events?rsid="+ rsid)
    r = requests.get(search_url, auth=('hector', 'hector'))

    return r.json()
    #return json.dumps(r.json(), sort_keys=True,indent=4, separators=(',', ': '))




#print "RSID is: "+ initiateSearch()
print "### search.py executed #####"
#getSearchResults(initiateSearch())