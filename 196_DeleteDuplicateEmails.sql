-- Person table:
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+

-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. 

CREATE TABLE Person (
    id int PRIMARY KEY,
    email varchar
);

INSERT INTO Person
('id', 'email')
VALUES 
('1', 'john@example.com'), 
('2', 'bob@example.com'), 
('3', 'john@example.com');


-- This almost works, but doesn't account for requirement of keeping the email with the smallest id
delete from Person
where id in (
    select id from (
        select id from Person
        group by email
        having count(id) > 1
        ) as t
    );

-- This works, keeping only the email with the smallest id
delete p1 from Person p1, Person p2
where p1.Email = p2.Email and p1.Id > p2.Id;