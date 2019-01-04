import requests
from pprint import pprint
import json
import sendMail


key='AIzaSyA--j1mjasUVSo3uExp8sgJjgIbnSiVKwk'
baseUrl = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

def constructUrl(origin,destination):
    global baseUrl,key
    delim = '&'
    url = baseUrl + 'origins=' + origin + delim
    url += 'destinations='+destination + delim
    url += 'key=' + key + delim
    url += 'mode=' +  'driving' + delim
    url += 'departure_time=now' + delim
    url += 'traffic_model=optimistic'
    return url

def sendRequest(url):
    response = requests.get(url)
    return response
    
def processResponse(response):
    if(response.status_code!=200):
        print 'Failed: '+ response.status_code
        return -1
    else:
        print 'OK.'
        data = json.loads(response.text)
        pprint(data)
        return int(data['rows'][0]['elements'][0]['duration']['value'])
    
# destination = 'SLVElegant+Bengaluru'
# origin = 'GE+Bengaluru'

destination = 'SJRSpencer+Bengaluru'
origin = 'Woohoo+Bengaluru'

url = constructUrl(origin,destination)
response = sendRequest(url)
time_taken = processResponse(response)
actual_time = 900


# if time_taken<actual_time:
#     sendMail.sendEmail(str(time_taken/60))