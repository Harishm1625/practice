select * from emp1;
select * from emp2;



select st_name,empid
from emp2
where st_no in (select st_no from emp2 where st_no in (1,2,3) )