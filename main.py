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
    elif(action=="root_faculty.faculty.faculty_info_by_name"):
        response=faculty_info_by_name(parameters.get('faculty_info_category'),
                                      parameters.get('faculty_first_name'),parameters.get('faculty_last_name'))
        pass
    # return a fulfillment response
    return response