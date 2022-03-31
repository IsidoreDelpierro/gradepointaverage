#!/usr/bin/python3
# neraTL - Taryuni's template library
# by Taryuni [http://about.me/isidoredelpierro/]
# Copyright 2019 Taryuni

import mysql.connector
import sys
#import time

__version__ = '1.0.0'


class gpaDB:
    
    connection = ""                 #private
    lastQuery = ""                  #public
    magicQuotesActive = False       #private
    realEscapeStringExists = False  #private
    database = ""                   #public
    
    def __init__(self, **kwargs):
        '''
            db = gpaDB( [ table = ''] [, filename = ''] )
            constructor method
                table is for CRUD methods 
                filename is for connecting to the database file
        '''
        # see filename setter below
        self.filename = kwargs.get('database')
        self.table = kwargs.get('table', '')
    ###########################################################

    def __iter__(self): #allows class to be called as an iterable generator
        cursor = self._db.cursor()
        cursor.execute(
            'SELECT * FROM {} ORDER BY id'
            .format(self._table))
        for row in cursor:
            yield dict(row)
    ###########################################################
    
    def createTables(self, cursor):
        '''
            db.create_tables(cursor)
            method for creating necessary tables for specific application
                cursor is cursor obtained from filename property declaration
        '''
        sqlAccounts = """CREATE TABLE IF NOT EXISTS accounts (
                        id INT(5) PRIMARY KEY AUTO_INCREMENT,
                        username VARCHAR(30) NOT NULL,
                        password VARCHAR(15) NOT NULL)"""
                        
        sqlConstants = """CREATE TABLE IF NOT EXISTS constants (
                        id INT(5) PRIMARY KEY AUTO_INCREMENT,
                        constant VARCHAR(2) NOT NULL,
                        value FLOAT NOT NULL)"""
                        
        sqlCourses = """CREATE TABLE IF NOT EXISTS courses (
                        id INT(5) PRIMARY KEY AUTO_INCREMENT,
                        code CHAR(6) NOT NULL,
                        title VARCHAR(60) NOT NULL,
                        status CHAR(1) NOT NULL,
                        value INT(2) NOT NULL)"""
                        
        sqlPrograms = """CREATE TABLE IF NOT EXISTS programs (
                        id INT(5) PRIMARY KEY AUTO_INCREMENT,
                        program VARCHAR(60) NOT NULL,
                        department VARCHAR(60) NOT NULL,
                        faculty VARCHAR(60) NOT NULL)"""
                        
        sqlResults = """CREATE TABLE IF NOT EXISTS results (
                        id INT(5) NOT NULL,
                        semester INT(1) NOT NULL,
                        level INT(3) NOT NULL,
                        code CHAR(6) NOT NULL,
                        grade VARCHAR(2) NOT NULL,
                        PRIMARY KEY (id, semester, level, code))"""
                        
        sqlSemesters = """CREATE TABLE IF NOT EXISTS semesters (
                        id INT(5) NOT NULL,
                        semester INT(1) NOT NULL,
                        level INT(3) NOT NULL,
                        gpa FLOAT NOT NULL,
                        PRIMARY KEY (id, semester, level))"""
                        
        sqlStudents = """CREATE TABLE IF NOT EXISTS students (
                        id INT(5) PRIMARY KEY NOT NULL,
                        matricule CHAR(8) NOT NULL,
                        fname VARCHAR(15) NOT NULL,
                        lname VARCHAR(15) NOT NULL,
                        program INT(2) NOT NULL,
                        cumgpa FLOAT NOT NULL)"""
                        
        sqlHonours = """CREATE TABLE IF NOT EXISTS honours (
                        id INT(5) PRIMARY KEY AUTO_INCREMENT,
                        honour VARCHAR(60) NOT NULL)"""
                        
        print('\nCREATING DATABASE TABLES.')
        #accounts table
        cursor.execute(sqlAccounts)
        if cursor: print('Table Successfully Created: accounts')
        else: print('Table Creation Unsuccessful: accounts')
        #constants table
        cursor.execute(sqlConstants)
        if cursor: print('Table Successfully Created: constants')
        else: print('Table Creation Unsuccessful: constants')
        #courses table
        cursor.execute(sqlCourses)
        if cursor: print('Table Successfully Created: courses')
        else: print('Table Creation Unsuccessful: courses')
        #programs table
        cursor.execute(sqlPrograms)
        if cursor: print('Table Successfully Created: programs')
        else: print('Table Creation Unsuccessful: programs')
        #results table
        cursor.execute(sqlResults)
        if cursor: print('Table Successfully Created: results')
        else: print('Table Creation Unsuccessful: results')
        #semesters table
        cursor.execute(sqlSemesters)
        if cursor: print('Table Successfully Created: semesters')
        else: print('Table Creation Unsuccessful: semesters')
        #students table
        cursor.execute(sqlStudents)
        if cursor: print('Table Successfully Created: students')
        else: print('Table Creation Unsuccessful: students')
        #honours table
        cursor.execute(sqlHonours)
        if cursor: print('Table Successfully Created: honours')
        else: print('Table Creation Unsuccessful: honours')
        
        print('\nDone creating tables.\n_____________________')
        
    
    def populate_database(self):
        '''
            db.populate_database()
            method for inserting default data into the application, for testing
        '''
        print('\nPOPULATING DATABASE.')
        #populate accounts table
        self.table = 'accounts'
        accounts = [
            dict(id = '', username = 'izzy', password = 'izzy'),
            dict(id = '', username = 'john', password = 'doe')
        ]
        print('... ', end = '')
        for account in accounts: self.insert(self.table, account)
        print('Done inserting into {} table'.format(self.table))
        
        #populate constants table
        self.table = 'constants'
        constants = [
            dict(id = '', constant = 'A', value = 4),
            dict(id = '', constant = 'B+', value = 3.5),
            dict(id = '', constant = 'B', value = 3),
            dict(id = '', constant = 'C+', value = 2.5),
            dict(id = '', constant = 'C', value = 2),
            dict(id = '', constant = 'D+', value = 1.5),
            dict(id = '', constant = 'D', value = 1),
            dict(id = '', constant = 'F', value = 0),
            dict(id = '', constant = 'I', value = 0),
            dict(id = '', constant = 'X', value = 0),
            dict(id = '', constant = 'W', value = 0)
        ]
        #print('Insert into table {}... '.format(self.table), end = '')
        print('... ', end = '')
        for constant in constants: self.insert(self.table, constant)
        print('Done inserting into {} table'.format(self.table))
        
        #populate courses table
        self.table = 'courses'
        courses = [
            dict(id = '', code = 'CEF201', title = 'Analysis', status = 'C', value = 4),
            dict(id = '', code = 'CEF203', title = 'Linear Algebra', status = 'C', value = 4),
            dict(id = '', code = 'CEF205', title = 'Introduction to Computing', status = 'C', value = 4),
            dict(id = '', code = 'CEF207', title = 'Programming I', status = 'C', value = 4),
            dict(id = '', code = 'CEF209', title = 'Discrete Mathematics', status = 'C', value = 4),
            dict(id = '', code = 'CEF211', title = 'Boolean Algebra and Logic Circuits', status = 'C', value = 4),
            dict(id = '', code = 'CEF217', title = 'Basic Electronics', status = 'C', value = 4),
            dict(id = '', code = 'CEF202', title = 'Computer Architecture', status = 'C', value = 4),
            dict(id = '', code = 'CEF204', title = 'Data Structures and Algorithms', status = 'C', value = 4)
        ]
        print('... ', end = '')
        for course in courses: self.insert(self.table, course)
        print('Done inserting into {} table'.format(self.table))
        
        #populate honours table
        self.table = 'honours'
        honours = [
            dict(id = '', honour = 'First Class Honours'),
            dict(id = '', honour = 'Second Class Upper Division'),
            dict(id = '', honour = 'Second Class Lower Division'),
            dict(id = '', honour = 'Third Class Degree'),
            dict(id = '', honour = 'Pass Degree')
        ]
        print('... ', end = '')
        for honour in honours: self.insert(self.table, honour)
        print('Done inserting into {} table'.format(self.table))
        
        #populate programs table
        self.table = 'programs'
        programs = [
            dict(id = '', program = 'Software Engineering', department = 'Computer Engineering', faculty = 'Faculty of Engineering and Technology'),
            dict(id = '', program = 'Network Engineering', department = 'Computer Engineering', faculty = 'Faculty of Engineering and Technology')
        ]
        print('... ', end = '')
        for program in programs: self.insert(self.table, program)
        print('Done inserting into {} table'.format(self.table))
        
        #populate results table
        self.table = 'results'
        results = [
            dict(id = 1, semester = 1, level = 200, code = 'CEF201', grade = 'D+'),
            dict(id = 1, semester = 1, level = 200, code = 'CEF203', grade = 'B+'),
            dict(id = 1, semester = 1, level = 200, code = 'CEF205', grade = 'C+'),
            dict(id = 1, semester = 1, level = 200, code = 'CEF207', grade = 'B'),
            dict(id = 1, semester = 1, level = 200, code = 'CEF209', grade = 'B'),
            dict(id = 1, semester = 1, level = 200, code = 'CEF211', grade = 'C'),
            dict(id = 1, semester = 1, level = 200, code = 'EEF217', grade = 'C+'),
            dict(id = 1, semester = 2, level = 200, code = 'CEF202', grade = 'B'),
            dict(id = 1, semester = 2, level = 200, code = 'CEF204', grade = 'B'),
            dict(id = 2, semester = 1, level = 200, code = 'CEF201', grade = 'D+'),
            dict(id = 2, semester = 1, level = 200, code = 'CEF203', grade = 'D+'),
            dict(id = 2, semester = 1, level = 200, code = 'CEF205', grade = 'D+'),
            dict(id = 2, semester = 1, level = 200, code = 'CEF207', grade = 'D+'),
            dict(id = 2, semester = 1, level = 200, code = 'CEF209', grade = 'D+'),
            dict(id = 2, semester = 1, level = 200, code = 'CEF211', grade = 'D+'),
            dict(id = 2, semester = 1, level = 200, code = 'EEF217', grade = 'D+'),
            dict(id = 2, semester = 2, level = 200, code = 'CEF202', grade = 'D+'),
            dict(id = 2, semester = 2, level = 200, code = 'CEF204', grade = 'D+')
        ]
        print('... ', end = '')
        for result in results: self.insert(self.table, result)
        print('Done inserting into {} table'.format(self.table))
        
        #populate semesters table
        self.table = 'semesters'
        semesters = [
            dict(id = 1, semester = 1, level = 200, gpa = 2.63),
            dict(id = 1, semester = 2, level = 200, gpa = 2.66),
            dict(id = 2, semester = 1, level = 200, gpa = 3.01),
            dict(id = 2, semester = 2, level = 200, gpa = 2.97)
        ]
        print('... ', end = '')
        for semester in semesters: self.insert(self.table, semester)
        print('Done inserting into {} table'.format(self.table))
        
        #populate students table
        self.table = 'students'
        students = [
            dict(id = 1, matricule = 'FE11A076', fname = 'Fonyuy', lname = 'Isidore', program = 1, cumgpa = 3.03),
            dict(id = 2, matricule = 'FE11A181', fname = 'Yufanyi', lname = 'Terrence', program = 2, cumgpa = 3.69)
        ]
        print('... ', end = '')
        for student in students: self.insert(self.table, student)
        print('Done inserting into {} table'.format(self.table))
        print('\nDone populating tables.\n_______________________')
        
    def create_tables(self, cursor):
        '''
            db.create_tables(cursor)
            method for creating necessary tables for specific application
                cursor is cursor obtained from filename property declaration
        '''
        student = 'student'
        images = 'images'
        
        sql = """CREATE TABLE IF NOT EXISTS student (
                id INT PRIMARY KEY AUTO_INCREMENT,
                firstName VARCHAR(20) NOT NULL,
                lastName VARCHAR(20),
                age INT,
                sex CHAR(1),
                gpa FLOAT)"""
        cursor.execute("DROP TABLE IF EXISTS {}".format(student))
        cursor.execute(sql)
        if cursor: print('Table Successfully Created: {}'.format(student))
        else: print('Table Creation Unsuccessful: {}'.format(student))
        
        sql = """CREATE TABLE IF NOT EXISTS images (
                id INT PRIMARY KEY,
                data MEDIUMBLOB)"""
        cursor.execute(sql)
        if cursor: print('Table Successfully Created: {}'.format(images))
        else: print('Table Creation Unsuccessful: {}'.format(images))
    ###########################################################
        
    def sql_do(self, sql, params = ()):
        '''
            db.sql_do( sql[, params])
            method for non-select queries
                sql is string containing SQL
                params is list containing parameters
            returning nothing
        '''
        cursor = self._db.cursor()
        cursor.execute(sql, params)
        self._db.commit()
    ###########################################################
    
    def sql_query(self, sql, params = ()):
        '''
            db.sql_query( sql[, params] )
            generator method for queries
                sql is string containing SQL
                params is list containing parameters
            returns a generator with one row per iteration
            each row is a Row factory
        '''
        cursor = self._db.cursor()
        cursor.execute(sql, params)
        for row in cursor:
            yield row
    ###########################################################
    
    def sql_row(self, sql, params = ()):
        '''
            db.sql_query_row( sql[, params] )
            query for a single row
                sql is string containing SQL
                params is list containing parameters
            returns a single row as a Row factory
        '''
        cursor = self._db.cursor()
        cursor.execute(sql, params)
        return cursor.fetchone()
    ###########################################################
    
    def sql_value(self, table, attribute, identifier):
        '''
            db.sql_query_row( attribute[, identifier] )
            query for a single value
                attribute is the attribute sought
                identifier is the id of the entry sought
            returns a single value
        '''
        cursor = self._db.cursor()
        self.table = table
        #use pos replacement & string concatenation to build query
        condition = ' WHERE id = {}'.format(identifier)
        query = 'SELECT {} FROM {} '.format(attribute, 
            self.table,
        )
        query += condition
        #print("\n", query, end = "")
        cursor.execute(query)
        return cursor.fetchone()[0]
        ###########################################################    
    
    def sql_set(self, table, record, orderby = []):
        '''
            db.sql_set(table, record, orderby)
            select a set of records from the table
                table is the table from which the data is retrieved
                record is a dict with key/value pairs corresponding to table schema
                orderby species the order in which results are arranged
        '''
        #print("This concerns the table {} ".format(table))
        cursor = self._db.cursor()
        self.table = table
        #using pos replacement & string concatenation to build query
        query = 'SELECT {} '.format(
            ', '.join(record[i] for i in range(len(record))),
        )
        target = 'FROM {} '.format(self.table)
        #if no order is specified, order by the first attribute
        order = 'ORDER BY {}'.format(orderby if orderby else record[0])
        query += target + order
        #print("\n", query, end = "")
        cursor.execute(query)
        #self._db.commit()
        return cursor.fetchall()
    ###########################################################
    
    def getrec(self, table, identifier):
        '''
            db.getrec(table, identifier)
            get a single row, by id
        '''
        cursor = self._db.cursor()
        self.table = table
        #use pos replacement & string concatenation to build query
        condition = ' WHERE id = {}'.format(identifier)
        query = 'SELECT * FROM {} '.format(
            self.table,
        )
        query += condition
        #print("\n", query, end = "")
        cursor.execute(query)
        return cursor.fetchone()
        ###########################################################
        
    def getrecs(self, table):
        '''
            db.getrecs(table)
            get all rows, returns a generator or Row factories
        '''
        cursor = self._db.cursor()
        self.table = table
        query = 'SELECT * FROM {}'.format(self.table)
        #print(query)
        cursor.execute(query)
        #print(type(c))        
        #c = cursor.execute(query)
        rows = cursor.fetchall()
        #print(rows)
        #for row in rows:
            #print(row)
            #yield row
        return rows   
    
    def insert(self, table, record):
        '''
            db.insert(table, record)
            insert a single record into the table
                record is a dict with key/value pairs corresponding to table schema
            omit id column to let MySQL generate it
        '''
        #print("This concerns the table {} ".format(table))
        cursor = self._db.cursor()
        self.table = table
        keylist = sorted(record.keys())
        values = [ record[v] for v in keylist] # a list of values ordered by key
        ###########################################################
        #using pos replacement & string concatenation to build query
        query = 'INSERT INTO {} ({}) VALUES'.format(
            self.table,
            ', '.join(keylist),
        )
        params = " ("
        i = 0
        while i < len(keylist):
            current = values.pop(0)
            if isinstance(current, str):
                params += "'"#surround strings with quotes
                params += current
                params += "'"
            else:
                params += str(current)
            params += ", " if values else ")"
            i += 1
        query += params
        #print("\n", query, end = "")
        cursor.execute(query)
        self._db.commit()
        return cursor.lastrowid
    ###########################################################
    
    def update(self, table, identifier, record):
        '''
            db.update(table, identifier, record)
            update a row in a table
                identifier is the value of the id column for the row to be updated
                record is a dict with key/value pairs corresponding to table schema
        '''
        cursor = self._db.cursor()
        self.table = table
        keylist = sorted(record.keys())
        values = [ record[v] for v in keylist] #list of values ordered by key
        #use pos replacement & string concatenation to build query
        condition = ' WHERE id = {}'.format(identifier)
        query = 'UPDATE {} SET '.format(
            self.table,
        )
        params = ""
        while keylist: #while keylist is not empty
            params += keylist[0]
            params += " = "
            if isinstance(values[0], str):
                params += "'" #surround strings with quotes
                params += values[0]
                params += "'"
            else:
                params += str(values[0])
            values.pop(0)
            keylist.pop(0)
            if values: params += ", "
        query += params + condition
        #print("\n", query, end = "")
        cursor.execute(query)
        self._db.commit()
    ###########################################################
    
    def delete(self, table, identifier):
        '''
            db.delete(table, identifier)
            delete a row from the table, by id
        '''
        cursor = self._db.cursor()
        self.table = table
        #use pos replacement & string concatenation to build query
        condition = ' WHERE id = {}'.format(identifier)
        query = 'DELETE FROM {} '.format(
            self.table,
        )
        query += condition
        #print("\n", query, end = "")
        cursor.execute(query)
        self._db.commit()
    ###########################################################
    
    def countrecs(self, table):
        '''
            db.countrecs(table)
            count the records in the table
            returns a single integer value
        '''
        self.table = table
        query = 'SELECT COUNT(*) FROM {}'.format(self.table)
        cursor = self._db.cursor()
        cursor.execute(query)
        #count = cursor.fetchone()[0]
        #print(count)
        return cursor.fetchone()[0]
    ###########################################################
    
    ### filename property
    @property
    def filename(self):
        return self._dbFilename
    
    @filename.setter
    def filename(self, fn):
        self._dbFilename = fn
        self._db = mysql.connector.connect(host = 'localhost', database = 'mysql', user = 'root', password = '')
        
        cursor = self._db.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(self.filename))
        print('\nDATABASE CREATION.', end = '')
        if cursor:  #if success, close default and connect to new database
            print('\nDatabase Created Successfully: {}'.format(self.filename))
            self._db = mysql.connector.connect(host = 'localhost', database = self.filename, user = 'root', password = '')
            cursor = self._db.cursor()
        else:
            print('\nDatabase Creation Unsuccessful: {}'.format(self._db))
            self._db.close()
            
        self.create_tables(cursor)
        self.createTables(cursor)
        self.populate_database()
        
        
    @filename.deleter
    def filename(self):
        self.close()
        
    
    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'test'
    
    def close(self):
        self._db.close()
        del self._dbFilename
        
        
    
class Sessions:
    
    loggedIn = False; #private boolean
    id = 0 #public integer
    
    def __init__(self):
        #start session
        self.checkLogin()
        #if self.loggedIn:
            #actions to take right away if user is logged in
            #We shall use a different approach for that
            #continue
        #else:
            #continue #actions to take if user is not logged in
        
    def isLoggedIn(self):
        return self.loggedIn
    
    def login(self, user):
        #database should find user based on username/password
        if user:
            #self.id = SESSION['id'] = user.id
            self.loggedIn = True
    
    def logout(self, user):
        #unset(SESSION['id'])
        #unset(self.id)
        self.loggedIn = False
    
    def checkLogin(self):
        #if isset(SESSION['id']):
            #self.id = SESSION['id']
            #self.loggedIn = True
        #else:
            #unset(self.id)
            #self.loggedIn = False
        pass
        
    
class Headers:
    
    def __init__(self):
        pass
    
    def func(self):
        pass
    
class Leverage:
    
    def __init__(self):
        pass
    
    def func(self):
        pass
    
    
class Globals:
    
    def __init__(self):
        pass
    
    def instantiate(self, record):
        pass
    
    def hasAttribute(self, attribute):
        pass
    
    def findAll(self, table):
        pass
    
    def findBySQL(self, sql=""):
        pass
    
    
    
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            print("Running test function from command line:...")
            test()
        else:
            print("Running main with more than one argument:...")
            #try: print(saytime(*(sys.argv[1].split(':'))).words())
            #except TypeError: print("Invalid time ({})".format(sys.argv[1]))
    else:
        print("Running main as a an importable script:...")
        #print(saytime_t(time.localtime()).words())       
         
def test():
    #import os
    db = 'school'     # nera database
    t = 'student' # test template table
    
    records = [
        dict(firstName = 'John', lastName = 'Doe', age = 30, sex = 'M', gpa = 2.24),
        dict(firstName = 'Yensi', lastName = 'Nadesh', age = 18, sex = 'F', gpa = 3.65),
        dict(firstName = 'Parfaite', lastName = 'Kolone', age = 21, sex = 'F', gpa = 2.72),
        dict(firstName = 'Prof', lastName = 'Yenshu', age = 67, sex = 'M', gpa = 1.89),
        dict(firstName = 'Isidore', lastName = 'DelPierro', age = 27, sex = 'M', gpa = 3.03)
    ]

    print('version', __version__)
    
    print('Create database file {} ...'.format(db), end = ' ')
    #db = gpaDB( database = db, table = t )
    db = gpaDB( database = 'flash')
    
    #gpa = gpaDB( database = 'flash')
    #print('Done creating database.\n________________________')
    #####################################################################
    #print('Create table ... ', end='')
    #db.sql_do(' DROP TABLE IF EXISTS {} '.format(t))
    #db.sql_do(' CREATE TABLE {} ( id INTEGER PRIMARY KEY, string TEXT ) '.format(t))
    #print('Done.')
    #####################################################################
    print('\nNOW LET\'S RUN SOME TESTS. ', end = '')
    print('Insert into table ... ', end = '')
    for record in records: db.insert(t, record)
    print('Done.')
    
    print('\nRead from table ...')
    for row in db.getrecs(t): print(row)
    
    print('\nInsert an extra row ... ')
    newid = db.insert(t, dict(firstName = 'Hayley', lastName = 'Marshall', age = 49, sex = 'F', gpa = 1.21),)
    print(db.getrec(t, newid))
    print('Done')
    
    print('\nRead again from table ...')
    for row in db.getrecs(t): print(row)
    print('Done')
    
    print('\nUpdate table')
    db.update(t, newid, dict(lastName = 'Mikelson', gpa = 1.35))
    print(db.getrec(t, newid))
    print('Done')
    
    print('\nRead once more from table ...')
    for row in db.getrecs(t): print(row)
    print('Done')
    
    print('\nNew record entered ...')
    newid = db.insert(t, dict(firstName = 'Jane', lastName = 'Anne', age = 31, sex = 'F', gpa = 1.92),)
    for row in db.getrecs(t): print(row)
    
    print('\nSet of attributes:...')
    attributes = ['firstName', 'lastName', 'age', 'sex']
    for row in db.sql_set(t, attributes, 'age'): print(row)
    
    print('\n(id is {}'.format(newid), end = '')
    print(', her name is {}'.format(db.sql_value(t, 'firstName', newid)), end = '')
    print(', and she\'s {} years old)'.format(db.sql_value(t, 'age', newid)))
    print('Find the complete data below...')
    print(db.getrec(t, newid))
    print('\nNow delete it')    
    db.delete(t, newid)
    for row in db.getrecs(t): print(row)
    
    print("\nThere are {} entries on the {} table".format(db.countrecs(t), t))
    db.close()
    
if __name__ == "__main__": test()