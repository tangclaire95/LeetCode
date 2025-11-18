# Write your MySQL query statement below

SELECT name FROM Customer 
WHERE referee_id !=2 OR referee_id IS null;

# or 
# SELECT name FROM customer 
# WHERE referee_id <> 2 OR referee_id IS NULL; 