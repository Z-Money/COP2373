# Import numpy for statistical calculations
import numpy as np

# Function to display various statistics about passed exams
def display_stats(exam):
    # Round the first 3 calculations to 2 places
    print(f"Mean (Avg): {np.mean(exam):.2f}%")
    print(f"Median: {np.median(exam):.2f}%")
    print(f"Std Dev: {np.std(exam):.2f}")
    # Exam scores are integers, so no formatting necessary
    print(f"Min: {np.min(exam)}%")
    print(f"Max: {np.max(exam)}%")


# Main function to carry out program functionality
def main():
    # Initialize the data types from grades.csv, using established size limits
    dtype = [
        ("first", "U20"),
        ("last", "U20"),
        ("exam1", "i4"),
        ("exam2", "i4"),
        ("exam3", "i4")
    ]

    # Load the data in from grades.csv
    gradeData = np.loadtxt('grades.csv', delimiter=',', dtype=dtype,
                           skiprows=1)

    # Gather the exam grades into one array
    exams = [gradeData["exam1"], gradeData["exam2"], gradeData["exam3"]]
    # Initialize the exam names
    exam_names = ["Exam 1", "Exam 2", "Exam 3"]

    # Iterate over all 3 exams, displaying the statistics for each
    for i in range(3):
        currentExam = exams[i]
        currentExamName = exam_names[i]
        print(f"\n{currentExamName} Statistics:")
        display_stats(currentExam)


    # Combine all grades together for total statistics
    all_grades = np.concatenate(exams)

    # Display statistics for all grades combined
    print("\nOverall Statistics:")
    display_stats(all_grades)

    # Iterate over every exam, displaying who passed and failed
    for i in range(3):
        # Total the number of grades either passing (>=60) or failing (<60)
        passes = np.sum(exams[i] >= 60)
        fails = np.sum(exams[i] < 60)

        # Display the previously calculated number of passes/fails
        print(f"\n{exam_names[i]}:")
        print("Passed:", passes)
        print("Failed:", fails)


    # Calculate the total amount of passes and fails
    total_grades = all_grades.size
    total_passes = np.sum(all_grades >= 60)

    # Calculate and display the pass percentage across all exams
    pass_percentage = (total_passes / total_grades) * 100
    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")

if __name__ == "__main__":
    main()