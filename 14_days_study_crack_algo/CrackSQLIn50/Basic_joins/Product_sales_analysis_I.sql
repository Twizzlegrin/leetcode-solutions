select product_name, year, price from Sales as s
left join Product as e
on s.product_id = e.product_id