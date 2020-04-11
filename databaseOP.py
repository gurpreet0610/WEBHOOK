import sqlite3
import json

def faculty_info_by_name(faculty_info_category,faculty_first_name,faculty_last_name):
    full_name =faculty_first_name + " " +faculty_last_name
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT {} FROM facultyDetails WHERE Name = '{}';".format(faculty_info_category,full_name))
    rows = cursorObj.fetchall()
    if(faculty_info_category=="Description"):
        speech_response=rows[0][0]
    elif(faculty_info_category=="Room"):
        speech_response=full_name+" is usually present in room " + rows[0][0]
    elif(faculty_info_category=="Expertise"):
        speech_response=full_name+" is specialized in " + rows[0][0]
    elif(faculty_info_category=="Experience"):
        speech_response=full_name+" is having an experience" + rows[0][0]
    elif(faculty_info_category=="Designation"):
        speech_response=full_name+" is " + rows[0][0]
    elif(faculty_info_category=="Department"):
        speech_response=full_name+" belongs to " + rows[0][0] + " department"
    
    display_response =[["Name",faculty_info_category],[full_name,rows[0][0]]]
    
    
    return {"fulfillmentText": speech_response
                }
    

def faculty_information(name):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Description FROM facultyDetails WHERE Name = '{}';".format(name))
    rows = cursorObj.fetchall()
    return {'fulfillmentText': rows[0][0]}
def admissionBPIT(departments):
    rsp=""
    if(departments in ["Computer Science and Engineering", "Information Technology", "Electronics and Communication Engineering", "Electrical and Electronics Engineering" , "Bachelor of Technology"]):
        rsp="Irrespective of the Branch, the admission process depends on the candidate's JEE MAIN'S rank, Following which a candidate has to enrol for the counselling. There are rounds of counselling after which a candidate can take admission to the institute."
    elif(departments in ["Master of Business Administration","Bachelor of Business Administration" , "School of Business Administration"]):
        rsp="To get admission to SBA you have to apply for CET conducted by IPU. After that, you have to take part in counselling in which college is allotted to you according to your rank in the same."
    elif(departments in ["Applied Sciences", "Applied Physics" , "Applied Chemistry" , "Applied Mathematics" ,"Mechanics or Humanities"]):
        rsp="There is no direct way to enrol in this course as it is the part of the BTech course curriculum."
    elif(departments == "Lateral Entry"):
        rsp="The students having a diploma are admitted directly in the second year as per the branch preference and their gradings."
    return {'fulfillmentText': rsp}
def bpit_infrastructure_facility(infrastruture_facilities):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Description FROM infrafacility WHERE Facility = '{}';".format(infrastruture_facilities))
    rows = cursorObj.fetchall()
    return {'fulfillmentText': rows[0][0]}

# print(bpit_infrastructure_facility("class"))
# faculty_info_by_name("Description","Dr Bhawna","Suri")