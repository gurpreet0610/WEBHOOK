import sqlite3
import json

def navigation(room_id,req):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Stairs , Floor, Direction FROM RoomDetails WHERE RoomID = '{}';".format(room_id))
    rows = cursorObj.fetchall()
    response = "Take the stairs at your "+rows[0][0]+" then after reaching the "+rows[0][1]+" take your "+rows[0][2] +" to reach the destination displayed on the screen"
    try:
        print(req)
        req=req.get('queryResult').get("outputContexts")
        print(req)
        print(req[0][0].get('room_no.original'))
    except:
        pass
    return {"fulfillmentText": response  }
    
    
def faculty_name_by_dept_desg(departments,designation):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Name FROM facultyDetails WHERE Department = '{}' and Designation LIKE '%{}%';".format(departments,designation))
    rows = cursorObj.fetchall()
    if(len(rows)>1):
       response="There are multiple "+designation+"s in "+departments+" department for which the list is displayed on the screen"
    else:
        response=rows[0][0] +" is the " +designation+" of "+ departments +" department "
    return {"fulfillmentText": response  }
    
def faculty_general_by_name(faculty_first_name,faculty_last_name):
    full_name =faculty_first_name +" "+faculty_last_name
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Description FROM facultyDetails WHERE Name = '{}';".format(full_name))
    rows = cursorObj.fetchall()
    response=rows[0][0]
    return {"fulfillmentText": response  }
        
def departmentInfo(departments):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT About FROM info_departments WHERE Department = '{}';".format(departments))
    rows = cursorObj.fetchall()
    return {'fulfillmentText': rows[0][0]}

def departmentInfoCategory(departments,vision_mission_category):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT {} FROM info_departments WHERE Department = '{}';".format(vision_mission_category,departments))
    rows = cursorObj.fetchall() 
    return {'fulfillmentText': rows[0][0]}
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
        speech_response=full_name+" is having an experience of more than " + rows[0][0]
    elif(faculty_info_category=="Designation"):
        speech_response=full_name+" is " + rows[0][0]
    elif(faculty_info_category=="Department"):
        speech_response=full_name+" belongs to " + rows[0][0] + " department"
    
    return {"fulfillmentText": speech_response  }
    
def visionMissionBPIT(vision_mission_category):
    rsp=""
    if(vision_mission_category == "vision"):
        rsp="Our vision is to establish a leading global centre of excellence in multidisciplinary education, training and research in the area of Engineering, Technology and Management. To produce technologically competent and ethically sound professionals who excel in their field and dedicate themselves to the service of mankind."
    elif(vision_mission_category == "mission"):
        rsp="Our mission is to bridge the knowledge gaps, promote research culture among faculty and students and to honour the commitment towards social and moral values."
    elif(vision_mission_category == "vision and mission"):
        rsp="Our aim is to provide industry technologically sound, morally & emotionally strong professionals who practice commitment to their profession by imbibing corporate and research culture amongst our faculty and students so that they honour commitment towards social and moral values."
    elif(vision_mission_category == "quality policy"):
        rsp="We strive to breed excellence in all endeavours and impart quality education and training among our students and faculties matching the international standards."
    return {'fulfillmentText': rsp}

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
