import sqlite3

def faculty_name_expertise(department,expertise):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    if(department==""):
        cursorObj.execute("SELECT Name,Department,Designation FROM FacultyDetails WHERE Expertise LIKE '%{}%';".format(expertise))
    else:
        cursorObj.execute("SELECT Name,Department,Designation FROM FacultyDetails WHERE Expertise LIKE '%{}%' and Department LIKE '%{}%';".format(expertise,department))
    rows = cursorObj.fetchall()
    if(len(rows)==0):
        speech_response="Sorry, currently the faculty with expertise "+expertise+" is not found in my records."
    elif(len(rows)==1):
        name=rows[0][0]
        department=rows[0][1]
        designation=rows[0][2].split(',')[0]
        speech_response=rows[0][0]+", the "+designation+" of "+department+" department is expert in "+expertise
    elif(len(rows)>2 and len(rows)<=3):
        speech_response="Faculty expert in "+expertise+" are "+(', '.join(rows[x][0] for x in range(0,len(rows)-1)))+" and "+rows[len(rows)-1][0]
    else:
        speech_response="Faculty expert in "+expertise+" are "+(', '.join(rows[x][0] for x in range(0,len(rows))))+", etc."
    return {'fulfillmentText': speech_response} 

def snr_faculty_info_designation(category,designation):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    if category =="Description":
        cursorObj.execute("SELECT {},Name  FROM FacultyDetails WHERE Designation LIKE '%{}%';".format(category+"_Speech",designation))
    else:
        cursorObj.execute("SELECT {},Name  FROM FacultyDetails WHERE Designation LIKE '%{}%';".format(category,designation))   
    rows = cursorObj.fetchall()
    print(rows)
    full_name=rows[0][1]
    if(rows[0][0]==None):
        speech_response="Sorry, I could  not find the "+category+" of "+full_name+", the "+designation+" of BPIT in my records"
        return {'fulfillmentText': speech_response}
    else:
        if(category=="Description"):
            speech_response=rows[0][0]
        elif(category=="Room"):
            speech_response=full_name+", the "+designation+" of BPIT is present in room number " + str(rows[0][0])
        elif(category=="Expertise"):
            speech_response=full_name+", the "+designation+" of BPIT is specialized in " + rows[0][0]
        elif(category=="Experience"):
            speech_response=full_name+", the "+designation+" of BPIT is having an experience of more than " + str(rows[0][0])
        elif(category=="Designation"):
            speech_response=full_name+" is the "+designation+" of BPIT "
        elif(category=="Department"):
            speech_response=rows[0][0]
    return {'fulfillmentText': speech_response}

def faculty_info_department(category,department):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    if category == "Description":
        cursorObj.execute("SELECT {}  FROM FacultyDetails WHERE Department LIKE '%{}%';".format(category+"_Speech",department))
    else:
        cursorObj.execute("SELECT {}  FROM FacultyDetails WHERE Department LIKE '%{}%';".format(category,department))   
    rows = cursorObj.fetchall()
    if(category in ["Designation","Room","Experience"]):
        speech_response="Every faculty in "+department+" department has their own "+category+". Kindly try asking for a specific faculty."
    elif(category=="Department"):
        speech_response="Faculties belong to "+department
    elif(category=="Description"):
        speech_response="Our "+department+" faculty is highly professional and hard working. They are always trying to help their students in all ways." 
    else:
        results = ', '.join([rows[x][0] for x in range(len(rows))])
        results = ', '.join(results.split(', ')[0:3])
        if(category=="Name"):
            speech_response="The faculty of "+department+" department includes "+results+", etc."
        else:
            speech_response="The "+department+" department faculty's "+category+" includes "+results+", etc."
    return {'fulfillmentText': speech_response}

while(True):
    what = input('WHat? ')
    which = input('Which? ')
    print(faculty_info_department(what,which))


