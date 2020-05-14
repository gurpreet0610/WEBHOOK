import sqlite3
import json


def navigation(room_id,req):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Floor, Direction FROM RoomDetails WHERE RoomID = '{}';".format(room_id))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            rname=req.get('queryResult').get("outputContexts")[0].get('parameters').get("room_no.original")
            response = "After reaching the "+rows[0][0]+" take your "+rows[0][1] +" to reach the "+rname+" as displayed on your screen"
    except Exception as e:
        print(e)
        response = "Sorry, I am not able to find the room in my record."
    return {"fulfillmentText": response  }

def faculty_room_navigation(first_name,last_name):
    try:   
        full_name =first_name +" "+last_name
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Room,RoomID FROM FacultyDetails WHERE Name = '{}';".format(full_name))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            room=rows[0][1]
    except:
        room=-1
    try:
        cursorObj.execute("SELECT Floor, Direction FROM RoomDetails WHERE RoomID = '{}';".format(room))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            rname="room of "+full_name
            response = "After reaching the "+rows[0][0]+", take your "+rows[0][1] +" to reach the "+rname+" as displayed on your screen"
    except Exception as e:
        response = "Sorry, I am not able to find the room of "+full_name+" in my record."
    return {"fulfillmentText": response  }

def faculty_name_expertise(department,expertise):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if(department=="" or department==None):
            cursorObj.execute("SELECT Name,Department,Designation FROM FacultyDetails WHERE Expertise LIKE '%{}%';".format(expertise))
        else:
            cursorObj.execute("SELECT Name,Department,Designation FROM FacultyDetails WHERE Expertise LIKE '%{}%' and Department LIKE '%{}%';".format(expertise,department))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, currently the faculty with expertise "+expertise+" is not found in my records."
        elif(len(rows)==1):
            name=rows[0][0]
            department=rows[0][1]
            designation=rows[0][2].split(',')[0]
            response=rows[0][0]+", the "+designation+" of "+department+" department is expert in "+expertise
        elif(len(rows)>=2 and len(rows)<=3):
            response="Faculties expert in "+expertise+" are "+(', '.join(rows[x][0] for x in range(0,len(rows)-1)))+" and "+rows[len(rows)-1][0]
        else:
            response="Faculties expert in "+expertise+" are "+(', '.join(rows[x][0] for x in range(0,3)))+", etc."
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}


def faculty_info_dept_designation(category,department,designation):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if category =="Description":
            cursorObj.execute("SELECT {},Name FROM FacultyDetails WHERE Department LIKE '%{}%' and Designation LIKE '%{}%';".format(category+"_Speech",department,designation))
        else:
            cursorObj.execute("SELECT {},Name FROM FacultyDetails WHERE Department LIKE '%{}%' and Designation LIKE '%{}%';".format(category,department,designation))   
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        elif(len(rows)==1):
            full_name=rows[0][1]
            if(category=="Description"):
                response=rows[0][0]
            elif(category=="Room"):
                response=full_name+" is present in room " + rows[0][0]
            elif(category=="Expertise"):
                response=full_name+" is specialized in " + rows[0][0]
            elif(category=="Experience"):
                response=full_name+" is having an experience of more than " + rows[0][0]
            elif(category=="Designation"):
                response=full_name+" is the " + rows[0][0] + " of BPIT"
            elif(category=="Department"):
                response=full_name+" belongs to " + rows[0][0] + " department"
        else:
            response="There are multiple "+designation+"s in "+department+" department and their respective "+category+" is displayed on the screen"
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}

def faculty_info_department(category,department):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if category == "Description":
            cursorObj.execute("SELECT {}  FROM FacultyDetails WHERE Department LIKE '%{}%';".format(category+"_Speech",department))
        else:
            cursorObj.execute("SELECT {}  FROM FacultyDetails WHERE Department LIKE '%{}%';".format(category,department))   
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            if(category in ["Designation","Room","Experience"]):
                response="Every faculty in "+department+" department has their own "+category+". Kindly try asking for a specific faculty."
            elif(category=="Department"):
                response="Faculties belong to "+department
            elif(category=="Description"):
                response="Our "+department+" faculty is highly professional and hard working. They are always trying to help their students in all ways." 
            else:
                results = ', '.join([rows[x][0] for x in range(len(rows))])
                results = ', '.join(results.split(', ')[0:3])
                if(category=="Name"):
                    response="The faculty of "+department+" department includes "+results+", etc."
                else:
                    response="The "+department+" department faculty's "+category+" includes "+results+", etc."
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}

def snr_faculty_general_designation(designation):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM FacultyDetails where Designation LIKE '%{}%';".format(designation))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            response=rows[0][7]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {"fulfillmentText": response  }

def snr_faculty_info_designation(category,designation):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if category =="Description":
            cursorObj.execute("SELECT {},Name  FROM FacultyDetails WHERE Designation LIKE '%{}%';".format(category+"_Speech",designation))
        else:
            cursorObj.execute("SELECT {},Name  FROM FacultyDetails WHERE Designation LIKE '%{}%';".format(category,designation))   
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            full_name=rows[0][1]
            if(rows[0][0]==None):
                response="Sorry, I could  not find the "+category+" of "+full_name+", the "+designation+" of BPIT in my records"
                return {'fulfillmentText': response}
            else:
                if(category=="Description"):
                    response=rows[0][0]
                elif(category=="Room"):
                    response=full_name+", the "+designation+" of BPIT is present in room number " + str(rows[0][0])
                elif(category=="Expertise"):
                    response=full_name+", the "+designation+" of BPIT is specialized in " + rows[0][0]
                elif(category=="Experience"):
                    response=full_name+", the "+designation+" of BPIT is having an experience of more than " + str(rows[0][0])
                elif(category=="Designation"):
                    response=full_name+" is the "+designation+" of BPIT "
                elif(category=="Department"):
                    response=rows[0][0]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}

def faculty_general_dept_designation(departments,designation):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM FacultyDetails where Department LIKE  '%{}%' and Designation LIKE '%{}%';".format(departments,designation))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        elif(len(rows)>1):
            response="There are multiple "+designation+"s in "+departments+" department for which the list is displayed on the screen"
        else:
            response=rows[0][7]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {"fulfillmentText": response  }

def faculty_name_by_dept_desg(departments,designation):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Name FROM FacultyDetails WHERE Department LIKE '%{}%' and Designation LIKE '%{}%';".format(departments,designation))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        elif(len(rows)>1):
            response="There are multiple "+designation+"s in "+departments+" department for which the list is displayed on the screen"
        else:
            response=rows[0][0] +" is the " +designation+" of "+ departments +" department "
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    
    return {"fulfillmentText": response  }
    
def faculty_general_by_name(faculty_first_name,faculty_last_name):
    try:
        full_name =faculty_first_name +" "+faculty_last_name
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Description_Speech FROM FacultyDetails WHERE Name = '{}';".format(full_name))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            response=rows[0][0]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {"fulfillmentText": response  }

def faculty_info_by_name(category,faculty_first_name,faculty_last_name):
    try:
        full_name =faculty_first_name + " " +faculty_last_name
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if category =="Description":
            cursorObj.execute("SELECT {}  FROM FacultyDetails WHERE Name = '{}';".format(category+"_Speech",full_name))
        else:
            cursorObj.execute("SELECT {}  FROM FacultyDetails WHERE Name = '{}';".format(category,full_name))
        
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        elif(category=="Description"):
            response=rows[0][0]
        elif(category=="Room"):
            response=full_name+" is usually present in room " + rows[0][0]
        elif(category=="Expertise"):
            response=full_name+" is specialized in " + rows[0][0]
        elif(category=="Experience"):
            response=full_name+" is having an experience of more than " + rows[0][0]
        elif(category=="Designation"):
            response=full_name+" is the " + rows[0][0]
        elif(category=="Department"):
            response=full_name+" belongs to " + rows[0][0] + " department"
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "   
    return {"fulfillmentText": response  }
    
def sportsInfo(sports_social_activities):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Description FROM SportsActivities WHERE Name= '{}';".format(sports_social_activities))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            response = rows[0][0]  
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}

def societyInfoName(societies, society_category):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if(society_category == ""):
            cursorObj.execute("SELECT Description FROM SocietyDetails WHERE Name= '{}';".format(societies))
        else:
            cursorObj.execute("SELECT '{}' FROM SocietyDetails WHERE Name= '{}';".format(society_category,societies))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "    
        else:
            response = rows[0][0]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}

def societyInfoType(society_type):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Name, Description FROM SocietyDetails WHERE Type LIKE  '%{}%';".format(society_type))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        elif(len(rows)>1):
            response = "There are multiple socities working in "+society_type+" and the list is displayed on your screen"
        else:
            response =  rows[0][0]+" is working in the "+society_type+" domain. "+ rows[0][1]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}
       
def departmentInfo(departments):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT About_Speech FROM InfoDepartments WHERE Department = '{}';".format(departments))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            response = rows[0][0]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}

def departmentInfoCategory(departments,vision_mission_category):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        if vision_mission_category in ["Achievement", "Resources", "HOD"]:
            cursorObj.execute("SELECT {} FROM InfoDepartments WHERE Department = '{}';".format(vision_mission_category,departments))
        else:
            cursorObj.execute("SELECT {} FROM InfoDepartments WHERE Department = '{}';".format(vision_mission_category+"_Speech",departments))
        rows = cursorObj.fetchall() 
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            response = rows[0][0]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    return {'fulfillmentText': response}
    
def visionMissionBPIT(vision_mission_category):
    rsp=""
    if(vision_mission_category == "Vision"):
        rsp="Our vision is to establish a leading global centre of excellence in multidisciplinary education, training and research in the area of Engineering, Technology and Management."
    # To produce technologically competent and ethically sound professionals who excel in their field and dedicate themselves to the service of mankind    
    elif(vision_mission_category == "Mission"):
        rsp="Our mission is to bridge the knowledge gaps, promote research culture among faculty and students and to honour the commitment towards social and moral values."
    elif(vision_mission_category == "Vision and Mission"):
        rsp="Our aim is to provide industry technologically sound, morally & emotionally strong professionals."
    # who practice commitment to their profession by imbibing corporate and research culture amongst our faculty and students so that they honour commitment towards social and moral values
    elif(vision_mission_category == "Quality Policy"):
        rsp="We strive to breed excellence in all endeavours and impart quality education and training among our students and faculties matching the international standards."
    else:
        rsp="Sorry, I can try one more time if you ask me again. "
    
    return {'fulfillmentText': rsp}

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
    else:
        rsp="Sorry, I can try one more time if you ask me again. "
    
    return {'fulfillmentText': rsp}

def bpit_infrastructure_facility(infrastruture_facilities):
    try:
        con = sqlite3.connect('data.sqlite')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT Description FROM InfraFacility WHERE Facility = '{}';".format(infrastruture_facilities))
        rows = cursorObj.fetchall()
        if(len(rows)==0):
            response="Sorry, I can try one more time if you ask me again. "
        else:
            response = rows[0][0]
    except Exception as e:
        response="Sorry, I can try one more time if you ask me again. "
    
    return {'fulfillmentText': response}



