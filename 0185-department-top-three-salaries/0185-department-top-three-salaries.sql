# Write your MySQL query statement below
WITH RankedSalaries AS (
    SELECT 
        e.id AS employeeId,
        e.name AS employeeName,
        e.salary,
        e.departmentId,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM Employee e
)

SELECT
    d.name AS Department,
    r.employeeName AS Employee,
    r.salary AS Salary
FROM Department d
JOIN RankedSalaries r ON d.id = r.departmentId
WHERE r.salary_rank <= 3;