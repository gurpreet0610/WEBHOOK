from databaseOP import *


def results(req):
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
    elif(action=="root_bpit.bpit.infrastructure_facility"):
        response=bpit_infrastructure_facility(parameters.get('infrastruture_facilities'))
    # return a fulfillment response
    return {'fulfillmentText': response}