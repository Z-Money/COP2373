import inspect
import ZachariahKersey_ProgrammingExercise_1  # replace with your assignment name (without .py)

#replace docstring_example with your assignment name in the next 2 lines of code
with open("ZachariahKersey_ProgrammingExercise_1.txt", "w") as doc:
    doc.write(f"# Technical Design Document: "
              f"{ZachariahKersey_ProgrammingExercise_1.__name__}\n\n")
    #replace with your name, the date, and the description of the program
    doc.write(f"# Name: Zachariah Kersey\n")
    doc.write(f"# Date: January 17, 2026\n")
    doc.write(f"# Program Description: Handles the sale of 20 tickets\n\n")

    #replace docstring_example with your assignment name 
    for name, func in inspect.getmembers(ZachariahKersey_ProgrammingExercise_1,
                                         inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")
    
    #replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/Z-Money?tab=repositories")
print('Complete')