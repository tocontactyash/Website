# Import database module.
import json
import firebase_admin
from GSCrawler import get_from_GS
from firebase_admin import db
from firebase_admin import credentials

# Fetch the service account key JSON file contents ------------------------------------------------------------------
cred = credentials.Certificate("/Users/undi69/Desktop/Website/website-development-fcc87-firebase-adminsdk-rmhy7-9ba0ab20f4.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
     'databaseURL' : 'https://website-development-fcc87.firebaseio.com/'
})
# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/IndividualUsers')
    
# READING JSON TEMPLATE ----------------------------------------------------------

users_ref = ref.child('users')
with open('user_template.json') as json_file:
    data = json.load(json_file)
    users_ref.update(data)

with open('atanu.json') as json_file:
    data = json.load(json_file)
    # print (data['atanu']['email_id'])
    author  = get_from_GS(data['atanu']['name'])
    data['atanu']['interests'] = author.interests
    data['atanu']['publications']['title'] = [pub.bib['title'] for pub in author.publications]
    data['atanu']['publications']['url'] = [pub.bib['title'] for pub in author.publications]
    # print (data['atanu']['publications'])
    users_ref.update(data)
    # print (data['atanu'])




'''

with open('atanu.json') as json_file:
    # loaded_json = json.loads(json_file)
    for x in json_file:
	    print("%s: %d" % (x, json_file[x]))

'''
#SET
'''
users_ref = ref.child('users')
users_ref.set({
    'yash': {
        'author': 'Yash Yadati',
    },
    'atanu': {
        'author': 'Atanu Chatterjee',
    },
    'germano': {
        'author': 'Germano Iannachionne',
    },
})
'''
'''
#UPDATE
users_ref = ref.child('users')
users_ref.update({
    'yash': {
        'author': 'Yash Yadati',
        'level': 'Undergraduate',


    },
})

print(ref.get())
'''