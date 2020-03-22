import sqlite3

def faculty_information(name):
    con = sqlite3.connect('data.sqlite')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT Description FROM facultyProfile WHERE Name = '{}';".format(name))
    rows = cursorObj.fetchall()
    return rows[0][0]
        



# print(faculty_information("Ms Palak Girdhar"))