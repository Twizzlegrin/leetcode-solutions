SELECT s.user_id, ROUND(AVG(if(c.action="confirmed", 1, 0)),2) AS confirmation_rate
FROM Signups s 
LEFT JOIN Confirmations c 
ON s.user_id = c.user_id 
GROUP BY user_id