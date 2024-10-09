create table Employe (
id int,
name varchar(100),
age int,
salary int,
experiance int
);


select * from employe
insert into  Employe
(id,name,age,salary,experiance)
values(2,'raj',25,15000,3)

Alter table Employe
Add   yn varchar(100)

update Employe
set yn='yes' 
where id < 7



ALTER TABLE employe 
RENAME TO staff;


Alter table employe
add emp_name varchar(250)

update Employe
set emp_name='staff'
where experiance=2

update employe
set emp_name='office emp'
where experiance !=2

select salary from Employe
where emp_name='staff'


begin transaction
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);


CREATE TABLE Person1 (
    ID int ,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
   foreign key (ID) references  Persons(ID) 
);


insert into  Persons
(id,LastName,FirstName,Age)
values(8,'raj','deva',15)

select * from Person1
-


insert into  Person1
(id,LastName,FirstName,Age)
values(8,'raj','deva',15)


insert into  Person1
(id,LastName,FirstName,Age)
values(6,'raj','deva',15)








begin transaction
insert into  Persons
(id,LastName,FirstName,Age)
values(1,'raj','deva',15)


delete from Persons where id=1
select * from  Persons
begin transaction
rollback
commit










