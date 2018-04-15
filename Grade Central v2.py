from statistics import mean as m
import getpass

admins = {'yoid':'yopw', 'admin':'admin', 'Master Wayne':'Batman'}
studentDict = {'Alex':[99,92,96,92,90,94],
               'Brandon':[88,89,91,89,96,88],
               'Cassie':[77,72,75,84,76,92]}

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
    else:
        print('Student is not found in the system')

def avgGrade():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        average = round(m(gradeList), 2)

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
    else:
        print('command invalid, please try again')

login()