'''
Create a student grading system using Python that has the following functionalities:
1. Entering the grades of a student
2. Removing a student from the system
3. Calculating the average grades of a student

The user should be able to select whether he/she wants to remove a student, enter grades for a student of find the average grades.async

Also perform the following as part of this project:
 - There should be a log-in system to allow only admin access to the grading system
 - Make sure you use dictionaries and lists for storing student's data.
 - Us Python functions as much as you can
'''

from statistics import mean as m
import getpass


admins = {'yoid':'yopw', 'admin':'admin', 'Master Wayne':'Batman'}
studentDict = {'Alex':[99,92,96],
               'Brandon':[88,89,91],
               'Cassie':[77,72,75]}

def login():
    login = input('Username: ')
    if login in admins:
        pswd = getpass.getpass('Password: ')
        if admins[login] == pswd:
            print('Welcome, ', login)
            while True:
                main()
        else:
            print('Are you sure you are ' + login + ', GPS and IP scanning activated')
    else:
        print('Intruder Alert, your picture had been taken and submitted to the hall of failed break-in attempt')

def AddGrades():
    StudentName = input('Student Name: ')
    StudentGrade = input('Grade: ')

    if StudentName in studentDict:
        print('Adding Grade...')
        studentDict[StudentName].append(int(StudentGrade))
    else:
        print('Student does not exist. Please add the student before adding grade.')

def RemoveStudent():
    rmvStudent = input('Which student would you like to remove?: ')
    if rmvStudent in studentDict:
        print('Removing Student...')
        del studentDict[rmvStudent]

def avgGrade():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        average = m(gradeList)

        print(eachStudent, 'has an average grade of: ', average)

def AddAdmins():
    newAdmin = input('Admin Name: ')

    if newAdmin in admins:
        print('Admin is already registered.')
    else:
        newPass = input('Password: ')
        admins[newAdmin]=newPass
        print('New admin updated.')

def main():
    print ('''
    Welcome to Grade Central 

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Add Admin
    [5] - Exit
    ''')

    action = input('What would you like to do today? (Enter a number)')

    if action == '1':
        AddGrades()
    elif action == '2':
        RemoveStudent()
    elif action == '3':
        avgGrade()
    elif action == '4':
        AddAdmins()
    elif action == '5':
        exit()
    elif action == '0':
        print('0')
    else:
        print('command invalid, please try again')

login()