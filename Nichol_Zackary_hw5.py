# Name: Zackary Nichol
# Section: 9:30 CIS 115
# Project: Student Grading (hw5)
# Description: This student grader application allows a user to input the grades for any amount of assignments
# for any amount of students.

num_of_students = int(input("How many students will you be entering?: (int)"))

# Main dictionary to hold all student id, name, and grade information
student_database = {}

# Asks for the name and id for the user specified number of students
for i in range(0, num_of_students):
    student_name = input("What is student " + str(i + 1) + "'s name?: (string)")
    student_id = int(input("What is " + student_name + "'s id?: (int)"))
    student_database[str(student_id)] = student_name

# Asks for the amount of assignments given, then the grades from each student for those assignments
num_of_assignments = int(input("How many assignments were given?: (int)"))
for k, v in student_database.items():
    student_grades = []

    for q in range(0, num_of_assignments):
        invalid_input = True

        # Verifies that the grade given is valid between 0 and 100 (inclusive)
        while invalid_input:
            grade_input = float(input("For student " + v + ", enter assignment" + str(q) + " grade: (float 0-100)"))
            grade_input = float("{0:.2f}".format(grade_input))

            if not 0 <= grade_input <= 100:
                print("Invalid input, try again.")
            else:
                invalid_input = False
                student_grades.append(grade_input)

    # Fulfills the assignment requirement of having the dictionary value be a combination of student name and grades
    student_database[k] = student_database[k] + " " + str(student_grades)

    # Prints the average assignment score for the given student.
    average = 0
    for i in range(0, len(student_grades)):
        average += student_grades[i]
    average /= len(student_grades)

    print("Student " + student_database[k] + "'s average assignment grade is " + "{0:.1f}".format(average))
