from databaseOP import *


def results(req):
    action = req.get('queryResult').get('action')
    parameters=req.get('queryResult').get('parameters')
    response={'fulfillmentText': ''}

    if(action=="root_bpit.bpit.admission"):
        response= admissionBPIT(parameters.get('departments'))
    elif(action=="root_bpit.bpit.infrastructure_facility"):
        response=bpit_infrastructure_facility(parameters.get('infrastruture_facilities'))
    elif(action=="root_faculty.faculty.faculty_info_by_name"):
        response=faculty_info_by_name(parameters.get('faculty_info_category'),
                                      parameters.get('faculty_first_name'),parameters.get('faculty_last_name'))
    elif(action=="root_bpit.bpit.vision_mission"):
        response=visionMissionBPIT(parameters.get('vision_mission_category'))
    elif(action=="root_faculty.faculty.faculty_general_by_name"):
        response=faculty_general_by_name(parameters.get('faculty_first_name'),parameters.get('faculty_last_name'))
    elif(action=="root_department.department.about"):
        response=departmentInfo(parameters.get('departments'))
    elif(action=="root_department.department.categories"):
        response=departmentInfoCategory(parameters.get('departments'),parameters.get("vision_mission_category"))
    elif(action=="root_faculty.faculty.faculty_name_by_dept_desg"):
        response=faculty_name_by_dept_desg(parameters.get('departments'),parameters.get('faculty_dept_designation'))
    elif(action=="root_navigation.navigation.room"):
        response=navigation(parameters.get('room_no'),req)
    elif(action=="root_society.society.description_by_name"):
        response=societyInfoName(parameters.get("societies"),parameters.get("society_category"))
    elif(action=="root_society.society.name_by_type"):
        response=societyInfoType(parameters.get("society_type"))
    elif(action== "root_sports.sports.info"):
        response=sportsInfo(parameters.get("sports_social_activities"))
    elif(action== "root_faculty.faculty_general_by_dept_desg"):
        response=faculty_general_dept_designation(parameters.get("departments"),parameters.get("faculty_dept_designation"))
    elif(action=="root_faculty.faculty.snr_faculty_info_by_desg"):
        response=snr_faculty_info_designation(parameters.get("faculty_info_category"),parameters.get( "faculty_not_dept_designation"))
    elif(action=="root_faculty.faculty.snr_faculty_general_by_desg"):
        response=snr_faculty_general_designation(parameters.get("faculty_not_dept_designation"))
    elif(action=="root_faculty.faculty.faculty_info_by_dept"):
        response=faculty_info_department(parameters.get("faculty_info_category"),parameters.get('departments'))
    elif(action=="root_faculty.faculty.faculty_info_by_dept_desg"):
        response=faculty_info_dept_designation(parameters.get("faculty_info_category"),parameters.get('departments'),parameters.get("faculty_dept_designation"))
    elif(action=="root_faculty.faculty.faculty_name_by_expertise"):
        response=faculty_name_expertise(parameters.get('departments'),parameters.get("faculty_expertise"))
    elif(action=="root_faculty.faculty.faculty_room_navigation"):
        response=faculty_room_navigation(parameters.get("Faculty_First_Name"),parameters.get("Faculty_Last_Name"))

    # return a fulfillment response
    return response
