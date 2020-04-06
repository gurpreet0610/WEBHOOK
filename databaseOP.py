import sqlite3

def faculty_information(name):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Description FROM facultyProfile WHERE Name = '{}';".format(name))
    rows = cursorObj.fetchall()
    return rows[0][0]
        
def admissionBPIT(departments):
    if("Computer Science and Engineering" or "Information Technology" or "Electronics and Communication Engineering" or "Electrical and Electronics Engineering" or "Bachelor of Technology"):
        return "Irrespective of the Branch, the admission process depends on the candidate's JEE MAIN'S rank, Following which a candidate has to enrol for the counselling. There are rounds of counselling after which a candidate can take admission to the institute."
    elif("Master of Business Administration" or "Bachelor of Business Administration" or "School of Business Administration"):
        return "To get admission to SBA you have to apply for CET conducted by IPU. After that, you have to take part in counselling in which college is allotted to you according to your rank in the same."
    elif("Applied Sciences" or "Applied Physics" or "Applied Chemistry" or "Applied Mathematics" or   "Mechanics or Humanities"):
        return "There is no direct way to enrol in this course as it is the part of the BTech course curriculum."
    elif("Lateral Entry"):
        return "The students having a diploma are admitted directly in the second year as per the branch preference and their gradings."
# print(faculty_information("Ms Palak Girdhar"))