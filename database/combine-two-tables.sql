# Write your MySQL query statement below
# use 'outer join'  
# Since the 'personId' in table 'Address' is the foreign key of table 'Person', we can join these two tables to get the address information of a person.
# Considering there might be no address information for every person, we should use 'outer join' instead of the default 'inner join'.
# an 'outer join' is performed either using 'left join' or 'right join'. 
# Using the 'where' clause to filter the records will fail if there is no address information for a person because it will not display the name information.


select firstName, lastName, city, state 
from Person left join Address 
on Person.personID = Address.personID
;


