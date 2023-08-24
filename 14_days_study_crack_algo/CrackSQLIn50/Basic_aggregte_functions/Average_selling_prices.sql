SELECT
  u.product_id,
  ROUND(SUM(pr.price * u.units) / SUM(u.units), 2) AS average_price
FROM
  UnitsSold u
JOIN
  Prices pr ON u.product_id = pr.product_id AND u.purchase_date BETWEEN pr.start_date AND pr.end_date
GROUP BY pr.product_id
