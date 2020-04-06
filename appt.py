# import flask dependencies
from flask import Flask, request, make_response, jsonify
from databaseOP import * 


# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    response=""
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    parameters=req.get('queryResult').get('parameters')
    if(action == 'faculty_information'):
        faculty=parameters.get('faculty')
        response=faculty_information(faculty)
    elif(action == 'who_faculty'):
        departments=parameters.get('departments')
        faculty_dept_designation=parameters.get('faculty_dept_designation')
    elif(action=="root_bpit.bpit.admission"):
        response= admissionBPIT(parameters.get('departments'))
           
    # return a fulfillment response
    return {'fulfillmentText': response}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()