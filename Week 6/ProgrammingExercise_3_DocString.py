import inspect
import ZachariahKersey_ProgrammingExercise_3  # replace with your assignment name (without .py)

# replace docstring_example with your assignment name in the next 2 lines of code
with open("ZachariahKersey_ProgrammingExercise_3.txt", "w") as doc:
    doc.write(f"# Technical Design Document: "
              f"{ZachariahKersey_ProgrammingExercise_3.__name__}\n\n")
    # replace with your name, the date, and the description of the program
    doc.write(f"# Name: Zachariah Kersey\n")
    doc.write(f"# Date: February 17, 2026\n")
    doc.write(f"# Program Description: Analyzes a list of expenses to "
              f"find the total, highest, and lowest expenses.\n\n")

    # replace docstring_example with your assignment name
    for name, func in inspect.getmembers(ZachariahKersey_ProgrammingExercise_3,
                                         inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    # replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/Z-Money?tab=repositories")
print('Complete')