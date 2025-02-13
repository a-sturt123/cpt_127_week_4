'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''

with open('student_grades.csv', 'r') as infile:
    lines = infile.readlines()

grades = []
for line in lines[1:]:
    row = line.split(',')
    grades.append(float(row[3].strip()))

average_grade = sum(grades) / len(grades)

with open('student_grade_differences.csv', 'w') as outfile:
    outfile.write('id,first_name,last_name,grade,difference_from_average\n')
    for line in lines[1:]:
        row = line.split(',')
        grade = float(row[3].strip())
        difference = grade - average_grade
        outfile.write(f'{row[0]},{row[1]},{row[2]},{grade},{difference}\n')
