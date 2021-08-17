################################
""" Author: Karthik Sainadh """
################################

# import libs
import flask
from flask.helpers import make_response
from flask import request

app = flask.Flask(__name__)

@app.route('/notifyDeploy', methods=['POST'])
def notifyDeploy():
    dataRecieved = request.json
    if dataRecieved["status"] == True:
        print( "BUILD STAGE SUCCESS NOTE RECEIVED.. CALLING DEPLOYMENT AGENT" )
    else:
        print( "BUILD STAGE RETURNED FALSE" )
    return make_response('Success', 200)

app.run(host='0.0.0.0', port=9090)