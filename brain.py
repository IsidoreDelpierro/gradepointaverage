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
    def __init__(self, **kwargs):
        '''
            newStudent = Students( )
            constructor method
                takes no default arguments
        '''
        # see variable setters below
        self.table = 'students' 
        self.matricule = kwargs.get('matricule', '')
        self.db = gpaDB(database = 'flash')
        self.program = Programs()
    ########################################
    
    def findAll(self):
        '''
            newStudent.findAll()
            retrieve all students from the database
                takes no argument
        '''
        #rethink this algorithm. It's buggous
        programId = self.program.getProgramId(self.matricule)
        print(programId)
        condition = dict(pid = programId)
        print(condition)
        attributes = ['matricule', 'fname', 'lname', 'program', 'department', 'faculty', 'cumgpa']
        table = self.table +', programs'
        #for student in self.db.sql_features(table, attributes, condition): yield(student)
        for student in self.db.sql_set(table, attributes): yield(student)
    ########################################
    
    def findByMatricule(self, matricule):
        '''
            newStudent.findByMatricule()
            retrieves all info about a particular student
                matricule is the unique identifier of the student in question
        '''
        programId = self.program.getProgramId(matricule)
        condition = dict(matricule = matricule, pid = programId)
        attributes = ['matricule', 'fname', 'lname', 'program', 'department', 'faculty', 'cumgpa']
        table = self.table +', programs'
        for student in self.db.sql_features(table, attributes, condition): yield(student)
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
    
    def setHonour(self, cumgpa):
        '''
            newStudent.setHonour( cumgpa )
            receives a grade point average and uses it to determine the honour
                cumgpa is the student's cummulative gpa (on 4)
        '''
        if cumgpa >= 3.60 and cumgpa <= 4.00:
            honourCode = 1
        elif cumgpa >= 3.00 and cumgpa < 3.60:
            honourCode = 2
        elif cumgpa >= 2.50 and cumgpa < 3.00:
            honourCode = 3
        elif cumgpa >= 2.20 and cumgpa < 2.50:
            honourCode = 4
        elif cumgpa >= 2.00 and cumgpa < 2.20:
            honourCode = 5
        else:
            honourCode = -1
        #print('\n...from Students.setHonour()...\nHonour for {} is {}'.format(cumpga, honour))
        return honourCode
    ########################################
    
    def getHonour(self, honourCode):
        '''
            newStudent.getHonour( honourCode )
            receives an honour code and queries the database for the corresponding honour
                honourCode is and identifier that maps to the requested honour
        '''
        table = 'honours'
        selector = dict(id = honourCode)
        honour = self.db.sql_value(table, 'honour', selector)
        
        #print('\n...from Students.getHonour()...\n{} is a {}'.format(honourCode, honour))
        return honour
    ########################################
    @property
    def table(self): return self._dbTable
    @table.setter
    def table(self, t): self._dbTable = t
    @table.deleter
    def table(self): self._dbTable = 'test'
    
    def close(self):
        self._db.close()
        del self._dbTable
########################################

class Programs:
    def __init__(self):
        '''
            newProgram = Programs( )
            constructor method
                takes no default arguments
        '''
        # see variable setters below
        self.table = 'programs' 
        self.db = gpaDB(database = 'flash')
    ########################################
    
    def findAll(self):
        '''
            newProgram.findAll()
            retrieve all programs from the database
                takes no argument
        '''
        attributes = ['program', 'department', 'faculty']
        for program in self.db.sql_set(self.table, attributes): yield(program)
    ########################################
    
    def findByProgram(self, programid):
        '''
            newProgram.findByProgram( programid )
            receives a constant and queries the database for the corresponding value
                programid is id of the program we're interested in
        '''
        condition = dict(pid = programid)
        program = self.db.sql_value(self.table, 'program', condition)
        
        #print('\n...from Programs.findByProgram()...\nThe program is {}'.format(program))
        return program
    ########################################
    def getProgramId(self, matricule):
        '''
            newProgram.getProgramId( matricule )
            receives the matricule of a student and queries the database 
            for the id of the program taken by the student
                programid is id of the program we're interested in
        '''
        table = 'students'
        condition = dict(matricule = matricule)
        programId = self.db.sql_value(table, 'prog', condition)
        
        #print('\n...from Programs.getProgramId()...\nprogramid is {}'.format(programId))
        return programId
    ########################################
    @property
    def table(self): return self._dbTable
    @table.setter
    def table(self, t): self._dbTable = t
    @table.deleter
    def table(self): self._dbTable = 'test'
    
    def close(self):
        self._db.close()
        del self._dbTable
    
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
        '''
            newCourse = Courses( )
            constructor method
                takes no default arguments
        '''
        # see variable setters below
        self.table = 'courses' 
        self.db = gpaDB(database = 'flash')
    ########################################
    
    def findAll(self):
        '''
            newCourse.findAll()
            retrieve all courses from the database
                takes no argument
        '''
        attributes = ['code', 'title', 'status', 'value']
        for constant in self.db.sql_set(self.table, attributes): yield(constant)
    ########################################
    
    def findByCode(self, courseCode):
        '''
            newCourse.findByCode( code )
            receives a course code and queries the database for info about the course
                courseCode is the unique identifier for the course in question
        '''
        selector = dict(code = courseCode)
        attributes = ['code', 'title', 'status', 'value']
        limit = 1
        courseInfo = self.db.sql_features(self.table, attributes, selector, limit)
        
        #print('\n...from Course.findByCode()...\n{}'.format(courseInfo))
        return courseInfo
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
        # see variable setters below
        self.table = 'constants' 
        self.db = gpaDB(database = 'flash')
    ########################################
    
    def findAll(self):
        '''
            newConstant.findAll()
            retrieve all constants from the database
                takes no argument
        '''
        attributes = ['constant', 'value']
        for constant in self.db.sql_set(self.table, attributes): yield(constant)
    ########################################
    
    def findByConstant(self, constant):
        '''
            newConstant.findByConstant( constant )
            receives a constant and queries the database for the corresponding value
                constant is the constant whose value week seek
        '''
        condition = dict(constant = constant)
        value = self.db.sql_value(self.table, 'value', condition)
        
        #print('\n...from Constants.findByConstant()...\n{} has a value of {}'.format(grade, value))
        return value
    ########################################
    
    def setGrade(self, total):
        '''
            newConstant.setGrade( total )
            receives a mark and uses it to determine the grade
                total is the student's total mark on 100
        '''
        if total >= 80 and total <= 100:
            grade = 'A'
        elif total >= 70 and total < 80:
            grade = 'B+'
        elif total >= 60 and total < 70:
            grade = 'B'
        elif total >= 55 and total < 60:
            grade = 'C+'
        elif total >= 50 and total < 55:
            grade = 'C'
        elif total >= 45 and total < 50:
            grade = 'D+'
        elif total >= 40 and total < 45:
            grade = 'D'
        elif total >= 0 and total < 40:
            grade = 'F'
        else:
            grade = 'X'
        #print('\n...from Constants.setGrade()...\nGrade for {} is {}'.format(total, grade))
        return grade
    ########################################
    
    def getGradePoint(self, grade):
        '''
            newConstant.getGradePoint( total )
            receives a grade and queries the database for the corresponding grade point
                grade is the grade obtained by the student
        '''
        gradePoint = self.findByConstant(grade)
        
        #print('\n...from Constants.getGradePoint()...\n{} has a value of {}'.format(grade, gradePoint))
        return gradePoint
    ########################################
    @property
    def table(self): return self._dbTable
    @table.setter
    def table(self, t): self._dbTable = t
    @table.deleter
    def table(self): self._dbTable = 'test'
    
    def close(self):
        self._db.close()
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
    
    table = 'students'
    matricule = 'FE11A076'
    newStudent = Students(matricule = matricule)
    print('Calling from testStudents()...')
    
    print('')
    for info in newStudent.findByMatricule(matricule): print(info)
    
    condition = dict(matricule = matricule)
    name = newStudent.db.sql_value(table, 'lname', condition)
    gpa = newStudent.db.sql_value(table, 'cumgpa', condition)
    
    
    honour = newStudent.getHonour(newStudent.setHonour(gpa))
    print('{}, with Reg. No.: {} is a {} student with GPA {}'.format(name, matricule, honour, gpa))
    print('\nAll students:')
    for student in newStudent.findAll(): print(student)
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
    
    matricule = 'FE11A076'
    program = newProgram.findByProgram(newProgram.getProgramId(matricule))
    print('\nStudent {} studies {}'.format(matricule, program))
    print('\nAll programs:')
    for program in newProgram.findAll(): print(program)
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
    
    courseCode = 'CEF201'
    newCourse = Courses()
    print('Calling from testCourses()...')
    
    print('\nAbout {}'.format(courseCode))
    courseInfo = newCourse.findByCode(courseCode)
    print(courseInfo)
    print('Returned as a ', type(courseInfo))
    print('\n\nAll courses:\n')
    for course in newCourse.findAll(): print(course)
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
    print('Calling from testConstants()...\n')
    
    total = 85
    grade = newConstant.setGrade(total)
    print('\n{} is {} grade'.format(total, grade))
    gradePoint = newConstant.getGradePoint(grade)
    print('{} grade has a value of {}'.format(grade, gradePoint))
    
    total = 57
    grade = newConstant.setGrade(total)
    print('\n{} is {} grade'.format(total, grade))
    gradePoint = newConstant.getGradePoint(grade)
    print('{} grade has a value of {}'.format(grade, gradePoint))
    
    total = 64
    grade = newConstant.setGrade(total)
    print('\n{} is {} grade'.format(total, grade))
    gradePoint = newConstant.getGradePoint(grade)
    print('{} grade has a value of {}'.format(grade, gradePoint))
    
    print('\nAll constants:')
    for constant in newConstant.findAll(): print(constant)
########################################

def test():
    '''
        test( )
        test method for application modules
            takes no argument
    '''
    # each method called tests one module    
    #testAccounts()
    #testStudents()
    #testPrograms()
    #testSemesters()
    testCourses()
    #testResults()
    #testConstants()
########################################

if __name__ == "__main__": test()