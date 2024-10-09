--joins

create table emp1(
id int, name varchar (100),empid int

primary key (id)
)


insert into emp1
(id,name,empid)
values(1,'loki',101)

insert into emp1
(id,name,empid)
values(2,'raja',102)

insert into emp1
(id,name,empid)
values(3,'nira',103)


create table emp2(
st_no int,st_name varchar (100),empid int
primary key (st_no))


insert into emp2
(st_no,st_name,empid)
values(1,'krish',101)
insert into emp2
(st_no,st_name,empid)
values(2,'ragu',102)


insert into emp2
(st_no,st_name,empid)
values(3,'rex',103)

insert into emp2
(st_no,st_name,empid)
values(4,'rev',104)



select * from emp1
select * from emp2

-- inner join
select id ,name, st_no

from emp1
inner join emp2 on emp1.empid=emp2.empid


--left join
select * from emp1
select * from emp2

select id ,name
from emp1
left join emp2 on emp1.empid=emp2.empid

select * from emp1
select * from emp2
select id ,name,st_name,emp2.empid
from emp1
right join emp2 on emp1.empid=emp2.empid
