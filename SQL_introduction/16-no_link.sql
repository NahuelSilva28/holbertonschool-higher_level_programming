-- 16. Say my name
-- script that lists all records of the table "desc"
SELECT score, name
FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;

