import sqlite3

def faculty_information(name):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Description FROM facultyProfile WHERE Name = '{}';".format(name))
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
