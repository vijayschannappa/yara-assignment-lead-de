-- Write a SQL query to find the cancellation rate of requests with unbanned users
--  (both client and driver must not be banned) each day between "2013-10-01"and"2013-10-03".
--  Round Cancellation Rate to two decimal points. Return the result table in any order.

with temp_users as (select * from users where banned="No")
select tr.request_at as Day,round(sum(case when tr.status != 'completed' then 1 else 0 end)/count(tr.Id),2)
as cancellation_rate
from trips tr
inner join temp_users tu
on tr.client_id = tu.users_id
where tr.request_at between '2013-10-01' and '2013-10-03'
group by tr.request_at

