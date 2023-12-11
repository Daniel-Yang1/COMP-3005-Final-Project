#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2
import datetime


# In[5]:


#COMP 3005
#Daniel Yang 101194970

def getAllMembers():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
def getAllInstructors():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM instructors')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
        

def getAllRooms():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
    
def getAllEquipment():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equipment')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
def getAllClasses():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM classes')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    
def getActiveMembers():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members WHERE member_id in (select member_id from takes)')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
        
def addMember(first_name, last_name, reg_date, height, weight):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO members(first_name, last_name, registration_date, height, weight) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, reg_date, height, weight))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        
def addInstructor(first_name, last_name, salary):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO instructors(first_name, last_name, salary) VALUES (%s, %s, %s)"
        cursor.execute(sql, (first_name, last_name, salary))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()

def addClass(class_name, start_date, end_date):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO classes(class_name, start_date, end_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (class_name, start_date, end_date))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()

def assignClassToRoom(class_id, room_id, date):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO located_in(class_id, room_id, class_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (class_id, room_id, date))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()

def assignTrainer(member_id, instructor_id, sessions):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO trains(member_id, instructor_id, sessions_remaining) VALUES (%s, %s, %s)"
        cursor.execute(sql, (member_id, instructor_id, sessions))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        
        
def enrollInClass(class_id, member_id, registration_date):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO takes(class_id, member_id, registration_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (class_id, member_id, registration_date))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        
def updateEquipmentInspection(equipment_id, new_date):
    try:
        cursor = conn.cursor()
        sql = "UPDATE equipment SET last_inspection_date = (%s) WHERE student_id = (%s)"
        cursor.execute(sql, (new_date, equipment_id))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        
def deleteMember(student_id):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM students WHERE student_id = (%s)"
        cursor.execute(sql, (student_id,))
        print(cursor.statusmessage)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()


# In[6]:


if __name__ == '__main__':
    conn = psycopg2.connect("dbname=fitness user=postgres password=admin")
    while(1):
        print("Database Application")
        print("There are 5 options: ")
        print("1: Manage members")
        print("2: Manage classes")
        print("3: Manage instructors")
        print("4: Manage admin tasks")
        print("5: Exit")
        
        choice = input("Please make a selection: ")
        
        if choice == '1':
            while(1):
                print("There are 6 options: ")
                print("1: List all members")
                print("2: List all active (taking classes) members")
                print("3: Add a member")
                print("4: Assigning a personal trainer to a member")
                print("5: Enrolling a member in a class")
                print("6: Go back to main menu")
                choice = input("Please make a selection: ")
                if choice == '1':
                    getAllMembers()
                elif choice == '2':
                    getActiveMembers()
                elif choice == '3':
                    firstName = input("Please enter a first name: ")
                    print("")
                    lastName = input("please enter a last name: ")
                    print("")
                    height = input("Please enter a height: ")
                    print("")
                    weight = input("Please enter a weight: ")
                    print("")
                    reg_date = input("Please enter a date in YYYY-MM-DD format: ")
                    print("")
                    addMember(firstName, lastName, reg_date, height, weight)
                elif choice == '4':
                    member_id = input("Please enter a member ID")
                    print("")
                    instructor_id = input("Please enter an instructor ID")
                    print("")
                    assignTrainer(member_id, instructor_id, 10)
                elif choice == '5':
                    class_id = input("Please enter a class ID")
                    print("")
                    member_id = input("Please enter a member ID")
                    print("")
                    enrollmentDate = input("Please enter a date in YYYY-MM-DD format: ")
                    print("")
                    enrollInClass(class_id, member_id, enrollmentDate)
                else:
                    break
        elif choice == '2':
            while (1):
                print("There are 4 options: ")
                print("1: List all classes")
                print("2: Create a new class")
                print("3: Assign a class to a room")
                print("4: Go back to main menu")
                choice = input("Please make a selection: ")
                if choice == '1':
                    getAllClasses()
                elif choice == '2':
                    class_name = input("Please enter a class name: ")
                    print("")
                    start_date = input("Please enter a start date in YYYY-MM-DD format: ")
                    print("")
                    end_date = input("Please enter an end date in YYYY-MM-DD format: ")
                    print("")
                    addClass(class_name, start_date, end_date)
                elif choice == '3':
                    class_id = input("Please enter a class id: ")
                    print("")
                    room_id = input("Please enter a room id: ")
                    print("")
                    date = input("Please enter a class date in YYYY-MM-DD format: ")
                    print("")
                    assignClassToRoom(class_id, room_id, date)
                else:
                    break
        elif choice == '3':
            while (1):
                print("There are 3 options: ")
                print("1: List all instructors")
                print("2: Add an instructor")
                print("3: Go to main menu")
                choice = input("Please make a selection: ")
                if choice == '1':
                    getAllInstructors()
                if choice == '2':
                    firstName = input("Please enter a first name: ")
                    print("")
                    lastName = input("please enter a last name: ")
                    print("")
                    salary = input("Please enter a salary: ")
                    print("")
                    addInstructor(firstName, lastName, salary)
                else:
                    break
        elif choice == '4':
            while (1):
                print("There are 4 options: ")
                print("1: Get all rooms")
                print("2: Get all equipment")
                print("3: Update equipment inspection date")
                print("4: Go to main menu")
                choice = input("Please make a selection: ")
                if choice == '1':
                    getAllRooms()
                elif choice == '2':
                    getAllEquipment()
                elif choice == '3':
                    equipment_id = input("Please enter equipment ID: ")
                    print("")
                    date = input("Please enter an inspection date in YYYY-MM-DD format: ")
                    print("")
                    updateEquipmentInspection(equipment_id, new_date)
                else:
                    break
        elif choice == '5':
            conn.close()
            break
        else:
            print("Please enter a valid choice")

            
        
        
        


# In[ ]:




