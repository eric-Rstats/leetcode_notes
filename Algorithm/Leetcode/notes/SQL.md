
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

[1084. 销售分析III](https://leetcode.cn/problems/sales-analysis-iii/)


```
select
    t1.product_id, t2.product_name
from Sales t1, Product t2
where t1.product_id = t2.product_id
group by t1.product_id
# having sum(sale_date < '2019-01-01') = 0
# and sum(sale_date > '2019-03-31') = 0
having min(sale_date) between '2019-01-01' and '2019-03-31'
and max(sale_date) between '2019-01-01' and '2019-03-31'

```

[1045. 买下所有产品的客户](https://leetcode.cn/problems/customers-who-bought-all-products/)

```sql
SELECT 
    customer_id 
FROM 
    customer
GROUP BY customer_id
HAVING count(DISTINCT product_key) = (
    SELECT 
        count(DISTINCT product_key) 
    FROM product
)
```

[180. 连续出现的数字](https://leetcode.cn/problems/consecutive-numbers/)
```sql
select
    DISTINCT num as ConsecutiveNums
from
(
select
    id,
    num,
    row_number() over(partition by num order by id) as rn1,
    row_number() over(order by id) as rn2
from Logs
) t
group by num, rn2-rn1
having count(1) >= 3
```

[1321. 餐馆营业额变化增长](https://leetcode.cn/problems/restaurant-growth/)

窗口函数可以指定范围，比如过去一周滑动
```sql
SELECT visited_on, amount, average_amount
FROM
(SELECT
     visited_on,
     SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
     ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount, 
     ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
FROM
(SELECT
    visited_on,
    SUM(amount) AS amount
FROM Customer 
group by visited_on
) a
) b
WHERE b.rn >= 7
```

```sql
select visited_on, amount, average_amount
from (
select distinct visited_on, 
sum(amount) over(order by to_days(visited_on) range 6 preceding) amount, 
round(sum(amount) over(order by to_days(visited_on) range 6 preceding)/7, 2) average_amount
from Customer
order by visited_on) c 
where datediff(visited_on, (select min(visited_on) from Customer))>=6
```

[1484. 按日期分组销售产品](https://leetcode.cn/problems/group-sold-products-by-the-date/)
group_concat函数
```sql
select
    sell_date,
    count(distinct product) as num_sold,
    group_concat(distinct product) as products
from Activities
group by sell_date
order by 1
```

[1517. 查找拥有有效邮箱的用户](https://leetcode.cn/problems/find-users-with-valid-e-mails/)
正则
```sql
select *
from users 
where mail regexp '^[a-zA-A]+[a-zA-Z0-9_\\./\\-]*@leetcode\\.com$'

```