#601. Human Traffic of Stadium
#Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
#Return the result table ordered by visit_date in ascending order.
#The result format is in the following example.

with temp as (select id, row_number() over(order by id)  as rn,
id - row_number() over(order by id) as dif,
visit_date, people
from stadium
where people >= 100),
difs as (select dif, count(dif) as cnt from temp group by dif)
select id, visit_date, people from temp where dif in (select dif from difs where cnt >= 3);