#!usr/bin/python3

from access import gpaDB
from access import Globals

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
    
    def fullName(self):
        '''
            newStudent.fullName()
            uses the class-level variable (matricule) to retrieve the student's full name
                takes no argument
        '''
        condition = dict(matricule = self.matricule)
        #print('\nfrom Students.fullName()')
        attributes = ['fname', 'lname']
        for name in self.db.sql_features(self.table, attributes, condition, 1, 'fname'): yield(name)
    ########################################
    
    def getEnrollmentYear(self):
        '''
            newStudent.getEnrollmentYear()
            uses the class-level variable (matricule) to determine the student's faculty
                takes no argument
        '''
        #print('\nfrom newStudent.getEnrollmentYear() \nFaculty', self.matricule)
        yearCode = self.matricule[2] + self.matricule[3]
        #print(yearCode)
        year = '20' + yearCode
        
        return year
    ########################################
    
    def getFaculty(self):
        '''
            newStudent.getFaculty()
            uses the class-level variable (matricule) to determine the student's faculty
                takes no argument
        '''
        #print('\nfrom newStudent.getFaculty() \nFaculty', self.matricule)
        facultyCode = self.matricule[0] + self.matricule[1]
        #print(facultyCode)
        
        if facultyCode == 'AS':
            faculty = 'Applied School of Translators and Interpreters'
        elif facultyCode == 'AV':
            faculty = 'Faculty of Agriculture and Veterinary Medicine'
        elif facultyCode == 'CT':
            faculty = 'College of Technology'
        elif facultyCode == 'ED':
            faculty = 'Faculty of Education'
        elif facultyCode == 'FA':
            faculty = 'Faculty of Arts'
        elif facultyCode == 'FE':
            faculty = 'Faculty of Engineering and Technology'
        elif facultyCode == 'HS':
            faculty = 'Faculty of Health Science'
        elif facultyCode == 'LP':
            faculty = 'Faculty of Law and Political Science'
        elif facultyCode == 'SC':
            faculty = 'Faculty of Science'
        elif facultyCode == 'SM':
            faculty = 'Faculty of Social and Management Sciences'
        else:
            faculty = 'Doesn\'t exist. Not a valid faculty.'
        
        return faculty
    ########################################
    
    def programDuration(self):
        '''
            newStudent.programDuration()
            uses the class-level variable (matricule) to determine the student's program duration
                takes no argument
        '''
        #print('\nfrom newStudent.getFaculty() \nFaculty', self.matricule)
        facultyCode = self.matricule[0] + self.matricule[1]
        #print(facultyCode)
        
        if facultyCode == 'AS':
            duration = 4
        elif facultyCode == 'AV':
            duration = 4
        elif facultyCode == 'CT':
            duration = 3
        elif facultyCode == 'ED':
            duration = 3
        elif facultyCode == 'FA':
            duration = 3
        elif facultyCode == 'FE':
            duration = 4
        elif facultyCode == 'HS':
            duration = 6
        elif facultyCode == 'LP':
            duration = 4
        elif facultyCode == 'SC':
            duration = 3
        elif facultyCode == 'SM':
            duration = 3
        else:
            duration = 0
        
        return duration
    ########################################
    
    def getLevel(self):
        '''
            newStudent.getLevel()
            uses the class-level variable (matricule) to determine the student's level
                takes no argument
        '''
        enrollmentYear = self.getEnrollmentYear()
        thisYear = 2020
        years = thisYear - int(enrollmentYear)
        #print(int(enrollmentYear))
        duration = self.programDuration()
        #print(duration)
        
        if years == 1:
            level = 200
        elif years == 2:
            level = 300
        elif years == 3:
            level = 400
        elif years == 4:
            level = 500
        elif years == 5:
            level = 600
        elif years == 6:
            level = 700
        elif years == 7:
            level = 800
        else:
            level = years - duration
        #print('\nfrom newStudent.getLevel() \n{} is a level {}'.format(self.matricule, level))
        return level
    ########################################
    
    def validateMatricule(self):
        '''
            newStudent.validateMatricule()
            checks the class-level variable (matricule) to ensure that it conforms with the university's format
                takes no argument
        '''
        #print('\nfrom newStudent.validateMatricule())
        
        valid = True
        
        #print('has {} characters'.format(len(self.matricule)))
        if len(self.matricule) != 8:
            valid = False
            return valid
        #print('valid length')
        
        facultyCode = self.matricule[0] + self.matricule[1]
        print(facultyCode)
        if facultyCode == 'AS': pass
        elif facultyCode == 'AV':   pass
        elif facultyCode == 'CT':   pass
        elif facultyCode == 'ED':   pass
        elif facultyCode == 'FA':   pass
        elif facultyCode == 'FE':   pass
        elif facultyCode == 'HS':   pass
        elif facultyCode == 'LP':   pass
        elif facultyCode == 'SC':   pass
        elif facultyCode == 'SM':   pass
        else:   valid = False
        #print('valid faculty code')
        
        yearCode = self.matricule[2] + self.matricule[3]
        print(yearCode)
        if int(yearCode) <= 6: 
            valid = False
            return valid
        year = int('20' + yearCode)
        print(year)
        #print('valid year')
        
        listCode = self.matricule[4]
        print(listCode)
        if listCode == 'AS': pass
        elif listCode == 'A':   pass
        elif listCode == 'B':   pass
        elif listCode == 'C':   pass
        elif listCode == 'P':   pass
        elif listCode == 'D':   pass
        else:   valid = False
        #print('valid list')
        
        numberCode = self.matricule[5] + self.matricule[6] + self.matricule[7]
        print(numberCode)
        
        if int(self.matricule[5]) < 10: pass
        elif int(self.matricule[6]) < 10: pass
        elif int(self.matricule[7]) < 10: pass
        else: 
            valid = False
        #print('valid number')
        return valid
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
                honourCode is an identifier that maps to the requested honour
        '''
        table = 'honours'
        selector = dict(id = honourCode)
        honour = self.db.sql_value(table, 'honour', selector)
        
        #print('\n...from Students.getHonour()...\n{} is a {}'.format(honourCode, honour))
        return honour
    ########################################
    
    def getCummulativeGPA(self, matricule):
        '''
            newStudent.getCummulativeGPA( matricule )
            receives an honour code and queries the database for the corresponding honour
                matricule is the unique identifier for a particular student
        '''
        selector = dict(matricule = matricule)
        cummulativeGPA = self.db.sql_value(self.table, 'cumgpa', selector)
        
        #print('\n...from newStudent.getCummulativeGPA()...\n{} has a cummulative GPA of {}'.format(matricule, cummulativeGPA))
        return cummulativeGPA
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
    
    def __init__(self, **kwargs):
        '''
            newSemester = Semesters( )
            constructor method
                takes no default arguments
        '''
        # see variable setters below
        self.table = 'semesters' 
        self.matricule = kwargs.get('matricule')
        self.db = gpaDB(database = 'flash')
        #self.info = Globals(matricule = self.matricule)
        self.constant = Constants()
    ########################################
    
    def findAll(self):
        '''
            newSemester.findAll()
            retrieve from the database all semesters done by a particular student
                matricule is the unique identifier of the student whose semesters we want
        '''
        condition = dict(id = self.identifier)
        print(self.identifier)
        attributes = ['semester', 'level', 'gpa']
        for semester in self.db.sql_features(self.table, attributes, condition): yield(semester)
    ########################################
    
    def findBySemester(self, semester, level):
        '''
            newSemester.findBySemester(matricule, semester, level)
            receives a matricule, semester and level and queries the database for the corresponding semester
                matricule is the identifier for the student we're interested in
                semester is the semester number
                level is the student's current level
        '''
        condition = dict(id = self.identifier, semester = semester, level = level)
        semesterGPA = self.db.sql_value(self.table, 'gpa', condition)
        
        #print('\n...from Semesters.findBySemester()...\nThis semester, {} has a gpa of {}'.format(self.matricule, semesterGPA))
        
        
        condition = dict(id = self.identifier, semester = semester, level = level)
        attributes = ['semester', 'level', 'gpa']
        for semester in self.db.sql_features(self.table, attributes, condition): yield(semester)
        
        
        return semesterGPA
    ########################################
    
    def getSemesterGPA(self, semester, level):
        '''
            newSemester.getSemesterGPA(matricule, semester, level)
            receives a semester and level and queries the database for the corresponding semester
                semester is the semester number
                level is the student's current level
        '''
        condition = dict(id = self.identifier, semester = semester, level = level)
        semesterGPA = self.db.sql_value(self.table, 'gpa', condition)
        
        #print('\n...from Semesters.getSemesterGPA()...\nThis semester, {} has a gpa of {}'.format(self.matricule, semesterGPA))
        return semesterGPA
    ########################################
    
    def setSemesterGPA(self, semester, level):
        '''
            newSemester.setSemesterGPA(matricule, semester, level)
            receives a semester and level and queries the database for the corresponding results
                semester is the semester number
                level is the student's current level
        '''
        table = 'results'
        features = ['ca', 'exam', 'code']
        condition = dict(id = self.identifier, semester = semester, level = level)
        semesterResults = self.db.sql_features(table, features, condition)
        print(semesterResults)
        
        #print('\n...from Semesters.setSemesterGPA()...\n {}\'s results for this semester:\n{}'.format(self.matricule, semesterResults))
        print('') #total, totalMark, sumTotal
        totalMark = 0
        total = []
        sumTotal = 0
        creditLoad = 0
        gradeSum = 0
        loadSum = 0
        #gpa = 0
        for i in range(len(semesterResults)):
            print('')
            #print('pair is ', semesterResults[i])
            #print('index ', i)
            for j in semesterResults[i]:
                if isinstance(j, int): # use ca & exam to get total
                    print('mark = ', j)
                    totalMark += j
                    #print('sum is now ', totalMark)
                else: # use course code to get course's credit load
                    condition = dict(code = j)
                    print(j)
                    creditLoad = self.db.sql_value('courses', 'value', condition)
                    print('credit load = ', creditLoad)
                    loadSum += creditLoad
                    gradePoint = self.constant.getGradePoint(self.constant.setGrade(totalMark))
                    print('grade point is ', gradePoint)
                    gradeLoad = gradePoint * creditLoad
                    print('grade load is ', gradeLoad)
                    gradeSum += gradeLoad
                    print('gradeSum = ', gradeSum)
            #print('total mark is ', totalMark)
            total.append(totalMark)
            #print('total[{}] = {}, {} indices long'.format(i, total[i], len(total)))
            print('total[{}] = {}'.format(i, total[i]))
            totalMark = 0
            sumTotal += total[i]
            print('sumTotal = ', sumTotal)
            
        print('\nload sum = ', loadSum)
        print('grade sum = ', gradeSum)
        semesterGPA = round(gradeSum/loadSum, 2)
        #div = sumTotal/gradeSum
        print('Semester GPA = ', semesterGPA)
        
        status = self.db.update(self.table, dict(id = self.identifier, semester = semester, level = level), dict(gpa = semesterGPA))
        print('{} of type {}'.format(status, type(status)))
            
        return semesterGPA
    ########################################
    
    def setCummulativeGPA(self):
        '''
            newSemester.setCummulativeGPA()
            uses the class-level variable identifier to get semester gpa's
            and uses them to calculate cummulative gpa
                takes no argument
        '''
        print('from setCummulativeGPA()')
        attributes = ['gpa']
        gpaSum = 0
        count = 0
        #for row in self.db.sql_features(self.table, attributes, id = dict(self.identifier)): print(row)
        for gpa in self.db.sql_features(self.table, attributes, dict(id = self.identifier)): 
            print(gpa[0], ' is ', type(gpa[0])) 
            gpaSum += gpa[0]
            count += 1
            print(count, ': ', gpaSum)
            
        cummulativeGPA = round(gpaSum/count, 2)
        print('cummulative gpa = ', cummulativeGPA)
        table = 'students'
        
        self.db.update(table, dict(id = self.identifier), dict(cumgpa = cummulativeGPA))
        return cummulativeGPA
    ########################################
    
    def setStudentId(self, identity):
        '''
            newSemester.setStudentId(identity)
            receives an integeter and sets a class variable
                identity is the unique identifier that maps to the student we want
        '''
        self.identifier = identity
    ########################################
    
    def getStudentId(self, matricule):
        '''
            newSemester.getStudentId(matricule)
            receives a matricule and returns the corresponding id as recorded in the db
                matricule is the unique identifier of the student we want
        '''
        studentId = self.db.sql_value('students', 'id', dict(matricule = matricule))
        #print('{} has id {}'.format(matricule, studentId))
        return studentId
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
            newCourse.findByCode( courseCode )
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
    
    def insertCourse(self, courseCode, courseTitle, status, creditLoad):
        '''
            newCourse.insertCourse( courseCode, courseTitle, status, creditLoad)
            receives information about a course,
            verifies whether it's in the database, 
            and inserts it if it's not
                courseCode is the unique identifier for the course in question
                courseTitle is the name of the course
                status specifies whether the course is compulsory, elective or required
                creditLoad is the weight (in hours) attached to the course
        '''
        condition = dict(code = courseCode)
        try:
            courseCheck = self.db.getrec(self.table, dict(condition))
        except:
            print('Failed to retrieve {} from the database.'.format(courseCode))
            return -1
        else:
            if isinstance(courseCheck, tuple):  #course found in database, don't insert
                print('Can\'t insert a course that is already in the database')
                return -2
            else:   #course not found
                courses = [dict(id = '', code = courseCode, title = courseTitle, status = status, value = creditLoad)]
                for course in courses: newCourseId = self.db.insert(self.table, course)
                #print('Insert returned {} or type {}.'.format(newCourseId, type(newCourseId)))
                return newCourseId
    ########################################
    
    def editCourse(self, selector, features):
        '''
            newCourse.editCourse( selector, features)
            updates information about a course that exists in the database
                selector is a dictionary which hold selection conditions
                features is a dictionary which holds the data for update
        '''
        try:
            self.db.update(self.table, selector, features)
            
        except:
            return -1
        else:
            return 1
    ########################################
    
    def deleteCourse(self, courseCode):
        '''
            newCourse.deleteCourse( courseCode )
            receives a course code, 
            checks results to see if there are students taking the course, 
            then deletes the course if there aren't any
                courseCode is the unique identifier for the course we want to delete
        '''
        condition = dict(code = courseCode)
        table = 'results'
        try: #check if there are any results associated with the course
            courseCheck = self.db.getrec(table, dict(condition))
        except:
            print('Failed to retrieve {} from the database.'.format(courseCode))
            return -1
        else:
            if isinstance(courseCheck, tuple):  #there are students taking the course
                print('Can\'t delete course already taken by students.')
                return -2
            else:   #no students have taken the course yet
                self.db.delete(self.table, condition) #returns NoneType
                return 1
    ########################################
    
    
########################################

class Results:
    def __init__(self, **kwargs):
        '''
            newResult = Results( )
            constructor method
                takes no default arguments
        '''
        # see variable setters below
        self.table = 'results' 
        self.matricule = kwargs.get('matricule')
        self.semester = kwargs.get('semester', 1)
        self.level = kwargs.get('level', 200)
        self.db = gpaDB(database = 'flash')
        self.constant = Constants
    ########################################
    
    def findAll(self):
        '''
            newResult.findAll()
            retrieve from the database all results for a particular student
                takes no argument
        '''
        condition = dict(id = self.identifier)
        attributes = ['code', 'semester', 'level', 'ca', 'exam']
        for semester in self.db.sql_features(self.table, attributes, condition): yield(semester)
    ########################################
    
    def findBySemester(self, semester, level):
        '''
            newResult.findBySemester(semester, level)
            receives a semester and level and queries the database for the corresponding results
                semester is the semester number
                level is the student's current level
        '''
        #print('\n...from Results.findBySemester()...\n')
        
        condition = dict(id = self.identifier, semester = semester, level = level)
        attributes = ['code', 'semester', 'level', 'ca', 'exam']
        for semester in self.db.sql_features(self.table, attributes, condition): yield(semester)
    ########################################
    
    def viewResults(self, matricule):
        pass
    ########################################
    
    def totalMark(self, ca, exam, resit):
        pass
    ########################################
    
    def getGrade(self, courseCode, semester, level):
        '''
            newResult.getGrade(courseCode, semester, level)
            receives a course code, semester and level and queries the database for the corresponding results
                courseCode is the unique identifier for the course
                semester is the semester number
                level is the student's current level
        '''
        print('...from Results.getGrade()...')
        #collect ca & exam from results table
        #check if it's a resit 
        #if it is, average with exam
        #calculate grade
        if semester == 3:
            pass
        for grade in self.markFetcher(courseCode, semester, level): 
            ca = grade[0]
            exam = grade[1]
            print(ca, exam)
        total = ca + exam
        print('ca = {}: exam = {}: Total = {}.'.format(ca, exam, total))
        grade = self.constant.setGrade(total, total)
        #print(grade)
        return grade
    ########################################
    
    def markFetcher(self, courseCode, semester, level):
        '''
            newResult.markFetcher(courseCode, semester, level)
            receives a course code, semester and level and queries the database for the corresponding results
                courseCode is the unique identifier for the course
                semester is the semester number
                level is the student's current level
        '''
        print('...from Results.markFetcher()...')
        
        condition = dict(id = self.identifier, semester = semester, level = level, code = courseCode)
        attributes = ['ca', 'exam']
        for semester in self.db.sql_features(self.table, attributes, condition, 1): yield(semester)
    ########################################
    
    def setGrade(self, courseCode):
        pass
    ########################################
    
    def addCourse(self, courseCode, semester, level, ca = 0, exam = 0):
        '''
            newResult.addCourse( courseCode, studentId, semester, level)
            receives a course code, semester and level and checks for any results for that course
            if it doesn't find it the student can take the course
                courseCode is the unique identifier for the course in question
                semester is the semester in which the course is taken
                level is the student's current level
        '''
        try: #try inserting new results
            condition = dict(id = self.identifier, level = level, semester = semester, code = courseCode)
            try: #verify that the course is offered
                courseCheck = self.db.getrec('courses', dict(code = courseCode))
            except: #if db is inaccessible, abort
                print('{} Fatal Error: Exiting now.'.format(courseCode))
                return -1
            else: #if it's not offered, abort
                if isinstance(courseCheck, tuple):
                    pass
                #if courseCheck != 0:
                else:
                    print('{} of type {}.'.format(courseCheck, type(courseCheck)))
                    print('{} Unavailable: \nYou can\'t take a course the school doesn\'t offer.'.format(courseCode))
                    return -1
            #go on and add course
            results = [dict(id = self.identifier, semester = semester, level = level, code = courseCode, ca = ca, exam = exam)]
            for result in results: newResultId = self.db.insert(self.table, result)
        except:# has course been taken for this semester
            resultCheck = self.db.getrec(self.table, dict(condition))
            if isinstance(resultCheck, tuple):  #course already taken, don't add
                print('\n{} has already been taken in this semester.'.format(courseCode))
                return -2
            else: #error, abort
                print('Unknown result: {} of type {}.'.format(resultCheck, type(resultCheck)))
                #print('Result check returned {} of type {}.'.format(resultCheck, type(resultCheck)))
                return -3
        else: #course not yet taken, add
            print('Youpi: {} of type {}.'.format(newResultId, type(newResultId)))
            if newResultId == 0:
                print('Results for {} successfully inserted.'.format(courseCode))
                try:
                    resultCheck = self.db.getrec(self.table, dict(condition))
                except:
                    print('Failed to retrieve {} from the database.'.format(courseCode))
                    return -1
                else:
                    print('\nfrom Results.addCourse()...\n{} '.format(resultCheck))
            else: #error, abort
                print('{} inserted, but with unknown return type. Check! {}\n'.format(courseCode, newResultId))
                return -3
            return newResultId
    ########################################
    
    def dropCourse(self, courseCode, semester, level):
        '''
            newResult.dropCourse( courseCode, studentId, semester, level)
            receives info about a course and deletes corresponding results for it
            checks for results for the course in that semester,
            deletes from results table if found,
            checks for any other occurrence on results table,
            deletes course from courses table if no other result is found
                courseCode is the unique identifier for the course in question
                semester is the semester in which the course is taken
                level is the student's current level
        '''
        condition = dict(code = courseCode, semester = semester, level = level)
        try: #check if there are any results associated with the course, for this semester
            resultCheck = self.db.getrec(self.table, dict(condition))
        except:
            print('{}: AlphaError! Abort mission.'.format(courseCode))
            return -1
        else:
            print('\n{}: Returned {} of type {}'.format(courseCode, resultCheck, type(resultCheck)))
            if isinstance(resultCheck, tuple): #if results found
                print('Result Check is a tuple')
                try:    #try to drop course
                    deleteResult = self.db.delete(self.table, condition)
                except:
                    print('{}: Unable to drop course.'.format(courseCode))
                    return -1
                else:   #next
                    print('\n{}: Results deleted: {} of type {}.'.format(courseCode, deleteResult, type(deleteResult)))
                    try:    #check for any other results
                        resultCheck = self.db.getrec(self.table, dict(condition))
                    except:
                        print('{}: BetaError! Abort mission.'.format(courseCode))
                        return -2
                    else:
                        if isinstance(resultCheck, tuple): #another result found
                            pass
                        else:   #proceed
                            condition = dict(code = courseCode)
                            try:    #remove course from list of courses
                                deleteCourse = self.db.delete('courses', condition)
                            except:
                                print('{}: GammaError! Failed to delete course.'.format(courseCode))
                                return -3
                            else:
                                print('{}: Successfully deleted. \nDelete returned {} of type {}.'.format(courseCode, deleteCourse, type(deleteCourse)))
                                return 0
            else:
                print('{} not taken this semester. \nNothing to drop.'.format(courseCode))
    ########################################
    
    def getMark(self, courseCode):
        pass
    ########################################
    
    def inputMark(self, courseCode, mark):
        pass
    ########################################
    
    def getSemesterGPA(self, semester, level):
        pass
    ########################################
    
    def getSemesterResults(self, semester, level):
        pass
    ########################################
    def setStudentId(self, identity):
        '''
            newSemester.setStudentId(identity)
            receives an integeter and sets a class variable
                identity is the unique identifier that maps to the student we want
        '''
        self.identifier = identity
    ########################################
    
    def getStudentId(self, matricule):
        '''
            newSemester.getStudentId(matricule)
            receives a matricule and returns the corresponding id as recorded in the db
                matricule is the unique identifier of the student we want
        '''
        studentId = self.db.sql_value('students', 'id', dict(matricule = matricule))
        #print('{} has id {}'.format(matricule, studentId))
        return studentId
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
        elif total >= 59 and total < 70:
            grade = 'B'
        elif total >= 54 and total < 59:
            grade = 'C+'
        elif total >= 49 and total < 54:
            grade = 'C'
        elif total >= 44 and total < 49:
            grade = 'D+'
        elif total >= 39 and total < 44:
            grade = 'D'
        elif total >= 0 and total < 39:
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
    print('\n########################################')
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
    print('\n########################################')
    print('TESTING STUDENTS:...\n_____________________')
    
    table = 'students'
    matricule = 'FE11A076'
    newStudent = Students(matricule = matricule)
    print('Calling from testStudents()...')
    
    print('')
    for info in newStudent.findByMatricule(matricule): print(info)
    
    print('\nFull Name from matricule', end='')
    #fullName = newStudent.fullName()
    #print('\n{}: {}.'.format(matricule, fullName))
    for name in newStudent.fullName(): print('\n{}: {}.'.format(matricule, name[0] + ' ' + name[1]))
    
    print('\nValidating matricule')
    valid = newStudent.validateMatricule()
    if valid:
        print('{} is a valid matriculation number'.format(matricule))
    else:
        print('{} is not a valid matriculation number'.format(matricule))
    
    print('\nFaculty from matricule', end='')
    faculty = newStudent.getFaculty()
    print('\n{} is in the {}.'.format(matricule, faculty))
    
    print('\nLevel from matricule')
    level = newStudent.getLevel()
    if level > 100:
        print('{} is a level {}.\n'.format(matricule, level))
    else:
        print('{} should have graduated {} years ago'.format(matricule, level))
    
    print('\nEnrollemnt year from matricule')
    year = newStudent.getEnrollmentYear()
    print('{} got in in the year {}.\n'.format(matricule, year))
    
    condition = dict(matricule = matricule)
    name = newStudent.db.sql_value(table, 'lname', condition)
    cumgpa = newStudent.getCummulativeGPA(matricule)
    
    honour = newStudent.getHonour(newStudent.setHonour(cumgpa))
    print('{}, with Reg. No.: {} is a {} student with GPA {}'.format(name, matricule, honour, cumgpa))
    print('\nAll students:')
    for student in newStudent.findAll(): print(student)
########################################

def testPrograms():
    '''
        testPrograms( )
        test method for operation of the Programs module
            takes no argument
    '''
    print('\n########################################')
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
    print('\n########################################')
    print('TESTING SEMESTERS:...\n_____________________')
    
    newSemester = Semesters(matricule = 'FE11A076')
    print('Calling from testSemesters()...')
    
    matricule = 'FE11A076'
    newSemester.setStudentId(newSemester.getStudentId(matricule))
    print(newSemester.table)
    print(newSemester.matricule)
    print(newSemester.identifier, '\n')
    
    semester = 1
    level = 200
    
    thisSemester = newSemester.findBySemester(semester, level)
    for item in thisSemester: print(item)
    
    semesterResults = newSemester.setSemesterGPA(semester, level)
    print('\nSemester results = {}\n'.format(semesterResults))
    
    semesterGPA = newSemester.getSemesterGPA(semester, level)
    print('Semester GPA = {}'.format(semesterGPA))
    print('\nAll Semesters:')
    for semester in newSemester.findAll(): print(semester)
    
    print('\nCummulative GPA:')
    newSemester.setCummulativeGPA()
    #for semester in newSemester.setCummulativeGPA(): print(semester)
########################################

def testCourses():
    '''
        testCourses( )
        test method for operation of the Courses module
            takes no argument
    '''
    print('\n########################################')
    print('TESTING COURSES:...\n_____________________')
    
    courseCode = 'CEF206'
    courseTitle = 'Numeric Analyses'
    status = 'C'
    creditLoad = 6
    newCourse = Courses()
    print('Calling from testCourses()...')
    
    print('\nAbout {}'.format(courseCode))
    courseInfo = newCourse.findByCode(courseCode)
    print(courseInfo, '; returned as a ', type(courseInfo), '\n')
    
    
    addedCourse = newCourse.insertCourse(courseCode, courseTitle, status, creditLoad)
    print('\nAdded course is {} of type {}'.format(addedCourse, type(addedCourse)))
    
    print('\n\nAll courses:\n')
    for course in newCourse.findAll(): print(course)
    
    updateList = dict(title = 'Numerical Analysis', value = 4)
    conditions = dict(code = 'CEF206', status = 'C')
    editedCourse = newCourse.editCourse(conditions, updateList)
    print('Edited course returned {} of type {}.'.format(editedCourse, type(editedCourse)))
    
    print('\n\nAll courses:\n')
    for course in newCourse.findAll(): print(course)
    
    deletedCourse = newCourse.deleteCourse(courseCode)
    print('\nDelete code for deleted course is {}.'.format(deletedCourse))
    print('\n\nAll courses:\n')
    for course in newCourse.findAll(): print(course)
########################################

def testResults():
    '''
        testResults( )
        test method for operation of the Results module
            takes no argument
    '''
    print('\n########################################')
    print('TESTING RESULTS:...\n_____________________')
    
    matricule = 'FE11A076'
    semester = 1
    level = 200
    newResult = Results(matricule = matricule)
    print('Calling from testResults()...')
    newResult.setStudentId(newResult.getStudentId(matricule))
    print(newResult.matricule)
    print(newResult.identifier)
    
    print('\nLevel {} Sem. {}: Results:'.format(level, semester))
    for result in newResult.findBySemester(semester, level): print(result)
    
    print('\nAdding a course to Form B')
    courseCode = 'CEF201'
    ca = 29
    exam = 68
    addCourse = newResult.addCourse(courseCode, semester, level, ca, exam)
    print(addCourse, type(addCourse))
    
    grade = newResult.getGrade(courseCode, semester, level)
    print('\n{} in {}'.format(grade, courseCode))
    
    courseCode = 'CEF211'
    print('\nDropping course')
    dropCourse = newResult.dropCourse(courseCode, semester, level)
    print('The test returned {} of type {}\n'.format(dropCourse, type(dropCourse)))
    
    print('\nLevel {} Sem. {}: Results:'.format(level, semester))
    for result in newResult.findBySemester(semester, level): print(result)
    
    semester = 2
    print('\nLevel {} Sem. {}: Results:'.format(level, semester))
    for result in newResult.findBySemester(semester, level): print(result)
    
    print('\n{}: All results:'.format(matricule))
    for result in newResult.findAll(): 
        print('Level {}, Sem. {}: {}, ca = {}, exam = {}'.format(result[2], result[1], result[0], result[3], result[4]))
########################################

def testConstants():
    '''
        testConstants( )
        test method for operation of the Constants module
            takes no argument
    '''
    print('\n########################################')
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
    testAccounts()
    testStudents()
    testPrograms()
    testSemesters()
    testCourses()
    testResults()
    testConstants()
########################################

if __name__ == "__main__": test()