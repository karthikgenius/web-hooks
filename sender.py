################################
""" Author: Karthik Sainadh """
################################

# import libs
import requests
import time
import json

dataToSend = {'from':'AWS', 'stage':'build','status':True, 'timeTaken':'360'}

URL = 'http://localhost:9090/notifyDeploy'

requests.post(URL, data=json.dumps(dataToSend), headers={'Content-type':'application/json'})

print('EXITING BUILD STAGE in 5 seconds..')
time.sleep(5)
exit(0)

# REFERENCES
# https://stackoverflow.com/questions/11322430/how-to-send-post-request
# https://flask.palletsprojects.com/en/2.0.x/api/
# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request