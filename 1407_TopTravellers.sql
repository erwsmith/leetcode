-- Table: Users
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- +---------------+---------+
-- id is the primary key for this table.
-- name is the name of the user.
 
-- Table: Rides
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | user_id       | int     |
-- | distance      | int     |
-- +---------------+---------+
-- id is the primary key for this table.
-- user_id is the id of the user who traveled the distance "distance".
 
-- Write an SQL query to report the distance traveled by each user.
-- Return the result table ordered by travelled_distance in descending order, 
-- if two or more users traveled the same distance, 
-- order them by their name in ascending order

select Users.name, IFNULL(sum(Rides.distance), 0) as travelled_distance 
from Users left join Rides
on Users.id = Rides.user_id
group by Rides.user_id
order by travelled_distance desc, name asc;