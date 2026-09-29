# Student Marks, Grade and Performance Calculator

## Problem Statement

Students usually have to calculate their total marks, percentage, grade, and result separately. It can also be difficult to quickly find which subjects need more attention.

This project is made to solve this problem using Python. The program takes the details and marks of students, calculates their percentage and grade, checks whether they passed or failed, finds their weak subjects, and gives a simple performance description.

The program also compares the students and displays them according to their percentage so that the topper can be easily identified.

## What the Program Does

The program can:

- Take the student's name and registration number.
- Take marks for EVS, Calculus, and Programming.
- Check that the entered marks are between 0 and 100.
- Calculate the average percentage.
- Give a grade according to the percentage.
- Show whether the student passed or failed.
- Find subjects where the student scored below 20 marks.
- Give a performance level such as Excellent, Good, or Needs Improvement.
- Arrange the students according to their percentage.
- Display the topper.

## Grade System

| Percentage | Grade |
|---|---|
| 90 and above | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

## Performance Levels

| Percentage | Performance |
|---|---|
| 90 and above | Excellent |
| 80–89 | Very Good |
| 70–79 | Good |
| 60–69 | Satisfactory |
| 50–59 | Needs Improvement |
| Below 50 | Poor |

## Weak Subject

If a student gets less than 20 marks in a subject, that subject is shown as a weak subject. This helps the student understand which subject needs more attention.

## How the Program Works

First, the program asks for the student's name and registration number. Then it asks for marks in each subject.

The marks are checked so that invalid values are not accepted. After entering all the marks, the program calculates the average percentage and uses it to find the grade and performance level.

It also checks the marks of each subject. If the marks are below 20, that subject is added to the student's weak-subject list.

The program currently takes details for five students. After all the records are collected, the students are sorted from the highest percentage to the lowest percentage. Finally, their results are displayed along with their rank, and the student with the highest percentage is shown as the topper.

## Python Files Used

The project is divided into different files so that the code is easier to understand and manage.

- `main.py` – Handles the main program, takes student information, calculates the required details, sorts the students, and shows the final results.
- `grading.py` – Contains the functions used to calculate the grade and pass/fail result.
- `performance.py` – Gives a performance description based on the student's percentage.
- `display.py` – Displays the student's result, marks, grade, rank, and weak subjects.

## Expected Result

At the end, the program shows the results of all five students in rank order. For each student, it displays their percentage, grade, result, performance, subject-wise marks, and weak subjects.

The program also displays the name and percentage of the topper.

## Conclusion

This project is a simple way to manage student marks and results using Python. It reduces manual calculations and also gives useful information about a student's performance and weak subjects.
