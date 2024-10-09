create database school1
 use school1
create table studentt(
id int,
name varchar(20),
maths int,
tamil int,
eng int,
total int
);
 
insert into studentt VALUES (1,'mythili',90,30,20,400),
(2,'priya',80,20,20,350),
(3,'anu',90,30,40,400),
(4,'aruna',90,20,30,400),
(5,'dharu',80,50,40,304),
(6,'kalai',90,30,20,299),
(7,'kevin',90,30,20,307);
 
 
select * from studentt;
 
select ROW_NUMBER() OVER(partition by maths  ORDER BY total) rn


SELECT 
    id, 
    name,
    maths,
    tamil,
    eng,
    total ,
	row_number() OVER (PARTITION BY eng ORDER BY total DESC) AS rn
FROM studentt  
 ORDER BY id DESC;
 
 select
   id,
   tamil,
   total,
   row_number() over(partition by tamil ORDER  BY total desc) AS MM
 from studentt;
