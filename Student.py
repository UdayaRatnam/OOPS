class student:

    def __init__(self, name, studentID, gpa, year):
        self.name = name
        self.studentID = studentID
        self.gpa = gpa
        self.year = year

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setId(self, ID):
        self.studentID = ID
    def getID(self):
        return self.studentID
    def setGPA(self, grade):
        self.gpa = grade
    def getGPA(self):
        return self.gpa
    def setYear(self, year):
        self.year = year
    def getYear(self):
        return self.year


