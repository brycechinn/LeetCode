# Write your MySQL query statement below
SELECT stu.student_id, stu.student_name, sub.subject_name, IFNULL(grouped.attended_exams, 0) AS attended_exams
FROM Students stu
CROSS JOIN Subjects  sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM examinations
    GROUP BY student_id, subject_name
) grouped
ON stu.student_id = grouped.student_id AND sub.subject_name = grouped.subject_name
ORDER BY student_id, subject_name;