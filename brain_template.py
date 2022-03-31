#!usr/bin/python3

from access import gpaDB

class Accounts:
    def __init__(self):
        pass
    ########################################
    
    def authenticate(self, username, password):
        pass
    ########################################
    
    def findAll(self):
        pass
    ########################################
    
    def findByAccountId(self, mat):
        pass
    ########################################
########################################

class Students:
    def __init__(self):
        pass
    ########################################
    
    def findAll(self):
        pass
    ########################################
    
    def findByMatricule(self, matricule):
        pass
    ########################################
    
    def fullName(self, fname, lname):
        pass
    ########################################
    
    def getEnrollmentYear(self, matricule):
        pass
    ########################################
    
    def getFaculty(self, matricule):
        pass
    ########################################
    
    def getLevel(self, matricule):
        pass
    ########################################
    
    def validateMatricule(self, matricule):
        pass
    ########################################
    
    def setHonours(self, cumgpa):
        pass
    ########################################
    
    def getHonours(self, honour):
        pass
    ########################################
########################################

class Programs:
    def __init__(self):
        pass
    ########################################
    
    def findAll(self):
        pass
    ########################################
    
    def findByProgram(self, program):
        pass
    ########################################
    
########################################

class Semesters:
    
    def __init__(self):
        pass
    ########################################
    
    def findAll(self):
        pass
    ########################################
    
    def findBySemester(self, matricule, semester, level):
        pass
    ########################################
    
    def viewSemesterGPA(self, matricule, semester, level):
        pass
    ########################################
    
    def calculateSemesterGPA(self, matricule, semester, level):
        pass
    ########################################
    
    def getMark(self, courseCode):
        pass
    ########################################
    
    def inputMark(self, courseCode, mark):
        pass
    ########################################
    
    def getSemesterGPA(self, matricule, semester, level):
        pass
    ########################################
    
    def getSemesterResults(self, matricule, semester, level):
        pass
    ########################################
########################################

class Courses:
    def __init__(self):
        pass
    ########################################
    
    def findAll(self):
        pass
    ########################################
    
    def findByCode(self, courseCode):
        pass
    ########################################
    
    def addCourse(self, courseCode, courseTitle, status, creditLoad):
        pass
    ########################################
    
    def totalMark(self, ca, exam, resit):
        pass
    ########################################
    
    def getGrade(self, courseCode):
        pass
    ########################################
########################################

class Results:
    def __init__(self):
        pass
    ########################################
    
    def findAll(self):
        pass
    ########################################
    
    def findBySemester(self, matricule, semester, level):
        pass
    ########################################
    
    def viewResults(self, matricule):
        pass
    ########################################
########################################

class Constants:
    def __init__(self):
        '''
            newConstant = Constants( )
            constructor method
                takes no default arguments
        '''
        pass
    ########################################
    
    def findAll(self):
        '''
            newConstant.findAll()
            retrieve all constants from the database
                takes no argument
        '''
        pass
    ########################################
    
    def findByConstant(self, constant):
        '''
            newConstant.findByConstant( constant )
            receives a constant and queries the database for the corresponding value
                constant is the constant whose value week seek
        '''
        pass
    ########################################
    
    def setGrade(self, total):
        '''
            newConstant.setGrade( total )
            receives a mark and uses it to determine the grade
                total is the student's total mark on 100
        '''
        pass
    ########################################
    
    def getGradePoint(self, grade):
        '''
            newConstant.getGradePoint( total )
            receives a grade and queries the database for the corresponding grade point
                grade is the grade obtained by the student
        '''
        pass
    ########################################
    @property
    def table(self): return self._dbTable
    @table.setter
    def table(self, t): self._dbTable = t
    @table.deleter
    def table(self): self._dbTable = 'test'
    
    def close(self):
        del self._dbTable
########################################


def testAccounts():
    '''
        testAccounts( )
        test method for operation of the Accounts module
            takes no argument
    '''
    print('########################################')
    print('TESTING ACCOUNTS:...\n_____________________')
    
    newAccount = Accounts()
    print('Calling from testAccounts()...')
    print(type(newAccount))
########################################

def testStudents():
    '''
        testStudents( )
        test method for operation of the Students module
            takes no argument
    '''
    print('########################################')
    print('TESTING STUDENTS:...\n_____________________')
    
    newStudent = Students()
    print('Calling from testStudents()...')
    print(type(newStudent))
########################################

def testPrograms():
    '''
        testPrograms( )
        test method for operation of the Programs module
            takes no argument
    '''
    print('########################################')
    print('TESTING PROGRAMS:...\n_____________________')
    
    newProgram = Programs()
    print('Calling from testPrograms()...')
    print(type(newProgram))
########################################

def testSemesters():
    '''
        testSemesters( )
        test method for operation of the Semesters module
            takes no argument
    '''
    print('########################################')
    print('TESTING SEMESTERS:...\n_____________________')
    
    newSemester = Semesters()
    print('Calling from testSemesters()...')
    print(type(newSemester))
########################################

def testCourses():
    '''
        testCourses( )
        test method for operation of the Courses module
            takes no argument
    '''
    print('########################################')
    print('TESTING COURSES:...\n_____________________')
    
    newCourse = Courses()
    print('Calling from testCourses()...')
    print(type(newCourse))
########################################

def testResults():
    '''
        testResults( )
        test method for operation of the Results module
            takes no argument
    '''
    print('########################################')
    print('TESTING RESULTS:...\n_____________________')
    
    newResult = Results()
    print('Calling from testResults()...')
    print(type(newResult))
########################################

def testConstants():
    '''
        testConstants( )
        test method for operation of the Constants module
            takes no argument
    '''
    print('########################################')
    print('TESTING CONSTANTS:...\n_____________________')
    
    newConstant = Constants()
    print('Calling from testConstants()...')
    print(type(newConstant))
########################################

def test():
    '''
        test( )
        test method for application modules
            takes no argument
    '''
    # each method called tests one module    
    testAccounts()
    testStudents()
    testPrograms()
    testSemesters()
    testCourses()
    testResults()
    testConstants()
########################################

if __name__ == "__main__": test()