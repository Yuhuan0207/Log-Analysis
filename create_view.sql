-- 
-- create view `error_table` record the number of unsuccessful visits happened everyday
-- 
```
create view error_table as 
select log.time::date as date_only, count(*) as errors 
from log
where status not like '%200 OK'
group by date_only
order by errors desc;
```
-- 
-- create view `total_visit_table` record the number of total visits happened everyday
-- 
```
create view total_visit_table as
select log.time::date as date_only, count(*) as total_visit 
from log
group by date_only
order by total_visit desc;
```
-- 
-- create view `error_rate_table` record the percentage of unsuccessful visits everyday
-- 
```
create view error_rate_table as
select error_table.date_only, cast(error_table.errors as float)/cast(total_visit_table.total_visit as float) as "error_rate"
from error_table, total_visit_table
where error_table.date_only = total_visit_table.date_only
order by error_rate desc;
```