
[1280. 学生们参加各科测试的次数](https://leetcode.cn/problems/students-and-examinations/)

cross-join:
```sql
select
    t1.student_id,
    t1.student_name,
    t2.subject_name,
    count(t3.subject_name) as attended_exams
from Students t1
cross join Subjects t2
left join Examinations t3
on t1.student_id = t3.student_id and t2.subject_name = t3.subject_name
group by t1.student_id, t2.subject_name
order by t1.student_id, t2.subject_name
```


[570. 至少有5名直接下属的经理](https://leetcode.cn/problems/managers-with-at-least-5-direct-reports/)

group by 利用having语句
```sql
select
    name
from Employee
where id in(
select
    managerId
from Employee
where managerId is not null
group by managerId
having count(1) >= 5
```

[1934. 确认率](https://leetcode.cn/problems/confirmation-rate/)

用sumif代替sum case when
```sql
select
    t1.user_id,
    round(ifnull(sum(action='confirmed')/count(t2.time_stamp), 0),2) as confirmation_rate
from Signups t1
left join Confirmations t2
on t1.user_id = t2.user_id
group by t1.user_id
```

[1174. 即时食物配送 II](https://leetcode.cn/problems/immediate-food-delivery-ii/)

子查询
```sql
select
     round(sum(order_date=customer_pref_delivery_date)/count(1)*100,2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
select
    customer_id,
    min(order_date)
from Delivery
group by customer_id
)
```