# we need to return three columns according to the requirements of the problem.

SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000; 

