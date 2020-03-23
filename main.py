from databaseOP import faculty_information 


def results(req):
    action = req.get('queryResult').get('action')
    parameters=req.get('queryResult').get('parameters')
    if(action == 'faculty_information'):
        faculty=parameters.get('faculty')
        response=faculty_information(faculty)
    elif(action == 'who_faculty'):
        departments=parameters.get('departments')
        faculty_dept_designation=parameters.get('faculty_dept_designation')    
    # return a fulfillment response
    return {'fulfillmentText': response}