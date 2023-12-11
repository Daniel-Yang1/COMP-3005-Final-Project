The database I used was a previously used database called postgres with 
username postgres and password admin, though it was created locally.
Prior to running the script you will need to create a database with 
the same details as above. Or you must change the connection settings used
in the line 
conn = psycopg2.connect("dbname=fitness user=postgres password=admin")

I used the following statements to create the tables and populate them with some test data.

CREATE TABLE members (
member_id serial PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
registration_date DATE,
height INTEGER,
weight INTEGER);
CREATE TABLE instructors(
instructor_id serial PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
salary INTEGER);
CREATE TABLE classes(
class_id serial PRIMARY KEY,
class_name TEXT NOT NULL,
start_date DATE,
end_date DATE);
CREATE TABLE Rooms(
room_id serial PRIMARY KEY,
building_name TEXT NOT NULL,
capacity INTEGER);
CREATE TABLE equipment(
equipment_id serial PRIMARY KEY,
purchase_date DATE NOT NULL,
last_inspection_date DATE,
price INTEGER);
CREATE TABLE takes(
Class_ID INTEGER REFERENCES classes(class_id),
Member_ID INTEGER REFERENCES members(member_id),
Registration_date DATE,
PRIMARY KEY (class_id, member_id));
CREATE TABLE teaches(
class_ID INTEGER REFERENCES classes(class_id),
instructor_ID INTEGER REFERENCES instructors(instructor_id),
PRIMARY KEY (class_id, instructor_id));
CREATE TABLE located_in(
class_ID INTEGER REFERENCES classes(class_id),
room_ID INTEGER REFERENCES rooms(room_id),
class_date DATE, 
PRIMARY KEY (class_id, room_id));
CREATE TABLE trains(
member_ID INTEGER REFERENCES members(member_id),
instructor_ID INTEGER REFERENCES instructors(instructor_id),
sessions_remaining INTEGER, 
PRIMARY KEY (member_id, instructor_id));
CREATE TABLE holds(
equipment_ID INTEGER REFERENCES equipment(equipment_id),
room_ID INTEGER REFERENCES rooms(room_id),
PRIMARY KEY (equipment_id, room_id));
Some statements for populating tables:
insert into classes(class_name, start_date, end_date) values (“Climbing”, “2020-01-01”, “2020-12-31”);
insert into classes(class_name, start_date, end_date) values (“Cycling, “2020-01-01”, “2020-12-31”);
insert into classes(class_name, start_date, end_date) values (“Lifting”, “2020-01-01”, “2020-12-31”);
insert into classes(class_name, start_date, end_date) values (“Running”, “2020-01-01”, “2020-12-31”);
insert into members(first_name, last_name, registration_date, height, weight) values ('Bob', 'Charlie', '2020-01-01', 180, 70);
insert into members(first_name, last_name, registration_date, height, weight) values ('Charlie', 'Delta', '2020-01-01', 185, 76);
insert into members(first_name, last_name, registration_date, height, weight) values ('Delta', 'Echo', '2020-01-01', 170, 60);
insert into members(first_name, last_name, registration_date, height, weight) values ('Echo', 'Foxtrot', '2020-01-01', 150, 90);
insert into instructors(first_name, last_name, salary) values ('John', 'Smith', 70000);
insert into instructors(first_name, last_name, salary) values (Bob', 'Smith', 70000);
insert into rooms(building_name, capacity) values ('Building 1', 500);
insert into rooms(building_name, capacity) values ('Building 2', 1000);
insert into equipment(purchase_date, last_inspection_date, price) values ('2020-01-01', '2020-01-01', 10000);
insert into equipment(purchase_date, last_inspection_date, price) values ('2020-01-01', '2020-01-01', 7000);

The application can be run by running the following command in a terminal

py COMP3005FinalProject.py

Assuming you have setup python properly and a compatible postgres database.


