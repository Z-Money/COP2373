import csv

def gatherInputs():
    """
    Gather the total number of students, their names and their exam grades

    Parameters:
        None

    Variables:
        students (list): A list of students records
        numberOfStudents (int): Total number of students to keep records for
        firstName (str): First name of the student
        lastName (str): Last name of the student
        gradeOne(int): First exam grade
        gradeTwo(int): Second exam grade
        gradeThree(int): Third exam grade

    Logic:
        1. Gather the number of students to keep records for, handling
            input errors
        2. Loop through adding the names and exam grades for the number
            of students to the student records, handling input errors
        3. Run the writeToCSV function, passing the list of student records

    Returns:
        None
    """

    # Initializes the list of student records
    students = []

    # Ask for the number of students to keep records for until input is valid
    while True:
        # Get the number of students to keep records for
        numOfStudents = input("How many students would you like to enter grades for: ")

        # Try converting the number of students to an integer value
        try:
            numOfStudents = int(numOfStudents)
        # Ask user for another value upon error converting the value
        except ValueError:
            print("Please enter an integer value for the number of students.")
            continue
        # Break the loop once the number of students converts to valid integer
        else:
            break

    # Loop through asking for the names and grades of each student
    for i in range(numOfStudents):
        # Format the current student number for printing to user
        currentStudentNum = i + 1

        # Gather the first and last names of the student
        firstName = input(f"Enter student {currentStudentNum}'s first name: ")
        lastName = input(f"Enter student {currentStudentNum}'s last name: ")

        # Ask for the 3 exam grades for the student until inputs are valid
        while True:
            # Gather the 3 exam grades for the current student
            gradeOne = input(f"Enter student {currentStudentNum}'s first exam grade: ")
            gradeTwo = input(f"Enter student {currentStudentNum}'s second exam grade: ")
            gradeThree = input(f"Enter student {currentStudentNum}'s third exam grade: ")

            # Try converting the 3 exam grades to an integer value
            try:
                gradeOne = int(gradeOne)
                gradeTwo = int(gradeTwo)
                gradeThree = int(gradeThree)
            # Ask user for another value upon error converting values
            except ValueError:
                print("Please enter an integer value for their exam grades.")
                continue
            # Break the loop once the 3 exam grades converts to valid integers
            else:
                break

        # Append the gathered values to the student records
        students.append([firstName, lastName, gradeOne, gradeTwo, gradeThree])

    # Write the student records to a CSV file
    writeToCSV(students)


def writeToCSV(students):
    """
    Gather the total number of students, their names and their exam grades

    Parameters:
        students (list): A list of students records

    Variables:
        HEADER (list): A list of header row

    Logic:
        1. Open the grades.csv file
        2. Write header row and students records to the open grades.csv file

    Returns:
        None
    """

    # Create the header row for the CSV file
    HEADER = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]

    # Open the grades.csv file
    with open("grades.csv", "w", newline="") as csvFile:
        # Write the HEADER and student records to the CSV file
        writer = csv.writer(csvFile)
        writer.writerow(HEADER)
        writer.writerows(students)
    # Print a message upon successfully writing the records
    print("\nData successfully written to grades.csv.")


def readGrades():
    """
    Open the grades from a CSV file and display them in a table format

    Parameters:
        None

    Variables:
        reader (list): A list of header row

    Logic:
        1. Open the grades.csv file
        2. Print the header of the CSV file
        3. Print all the rows of values from the CSV file

    Returns:
        None
    """

    # Open the grades.csv file
    with open("grades.csv", "r", newline="") as csvFile:
        # Use the DictReader on the CSV file
        reader = csv.DictReader(csvFile)

        # Print the header row, using formatting to create a table setup
        print(f"\n{reader.fieldnames[0]:<15}{reader.fieldnames[1]:<15}"
              f"{reader.fieldnames[2]:<10}{reader.fieldnames[3]:<10}"
              f"{reader.fieldnames[4]:<10}")
        # Iterate over each row in the CSV file to print the names and exams
        for row in reader:
            print(f"{row['First Name']:<15}{row['Last Name']:<15}"
                  f"{row['Exam 1']:<10}{row['Exam 2']:<10}{row['Exam 3']:<10}")



if __name__ == "__main__":
    # Gather the inputs from the user for the students records
    gatherInputs()
    # Print a table of values from the saved CSV file
    readGrades()