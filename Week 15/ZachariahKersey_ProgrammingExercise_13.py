# Import sqlite3 for database connection and random for population simulation
import sqlite3, random
# Import pyplot to visualize population simulation
import matplotlib.pyplot as plt

# Function for main program functionality
def main():
    # Connect with the database and create the cursor
    conn = sqlite3.connect("population_ZK.db")
    cursor = conn.cursor()

    # Create the population table within the database if it doesn't yet exist
    cursor.execute("CREATE TABLE IF NOT EXISTS population (city TEXT, "
                     "year INTEGER, population INTEGER)")

    # Create the initial list of cities with all values
    CITIES = [{"name": "Boca Raton", "year": 2025, "population": 104232},
              {"name": "Bradenton", "year": 2025, "population": 58184},
              {"name": "Daytona", "year": 2025, "population": 92873},
              {"name": "Dover", "year": 2025, "population": 3038},
              {"name": "Miami", "year": 2025, "population": 509107},
              {"name": "Naples", "year": 2025, "population": 20683},
              {"name": "North Port", "year": 2025, "population": 101564},
              {"name": "Port Charlotte", "year": 2025, "population": 67412},
              {"name": "Riverview", "year": 2025, "population": 116251},
              {"name": "Sarasota", "year": 2025, "population": 57764},]

    # Iterate over inserting all the cities into the population table
    for city in CITIES:
        insertCity(cursor, city["name"], city["year"], city["population"])

    # List to hold info fetched from the population table
    allCities = []
    cursor.execute("SELECT city, year, population FROM population WHERE "
                   "year = 2025 ORDER BY city")
    # Fetch data from population table and store in allCities
    for city in cursor.fetchall():
        # Format the collected data in a standardized format
        allCities.append({"name": city[0], "year": city[1],
                          "population": city[2]})

    # Simulate the population for each city from the database
    for city in allCities:
        simulatePopulation(cursor, city)

    # Loop continuously to account for input errors
    while True:
        # Print out city options and prompt user to select one
        for index, city in enumerate(allCities):
            print(f"{index + 1}. {city["name"]}")
        requestedCity = input("Please pick a city from above (#): ")
        # Try/except to handle noninteger or invalid inputs
        try:
            requestedCity = int(requestedCity)
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            # Handle integer inputs that aren't on the printed list
            if requestedCity not in range(1, len(allCities) + 1):
                print("Please enter a valid option from above.")
                continue
            # Generate a plot based on the requested city
            generatePlot(cursor, allCities[requestedCity-1])
            # Prompt user to view another city. Continue if yes, end if no
            viewAnotherCity = input("Would you like to view another city "
                                    "(y/n): ")
            if viewAnotherCity.strip().lower() == "y":
                continue
            else:
                break

    # Commit all changes to the database and close the database connection
    conn.commit()
    conn.close()

# Function to insert a city into the database
def insertCity(cursor, city, year, population):
    query = f"INSERT INTO population VALUES ('{city}', {year}, {population})"
    cursor.execute(query)

# Function to simulate the population over 20 years for any city
def simulatePopulation(cursor, city):
    for i in range(1,21):
        # Generate the magnitude of population growth or decline
        populationChange = random.randint(-2, 2)
        # Convert population change to a rate
        populationChange = 1 + (populationChange / 100)
        # Select the latest population value for the specific city
        cursor.execute(f"SELECT population FROM population WHERE "
                       f"city='{city["name"]}' ORDER BY year DESC LIMIT 1")
        output = cursor.fetchone()
        # Calculate the new population value and insert into the database
        newPopulation = round(output[0] * populationChange)
        cursor.execute(f"INSERT INTO population VALUES ('{city["name"]}', "
                       f"{city["year"] + i}, {newPopulation})")

# Function to generate the plot to visualize population growth for a city
def generatePlot(cursor, city):
    # Select all the population values for a city by year
    cursor.execute(f"SELECT year, population FROM population WHERE "
                   f"city='{city["name"]}' ORDER BY year")
    output = cursor.fetchall()
    # Separate the selected values into lists of years and population values
    years = []
    populations = []
    for row in output:
        years.append(row[0])
        populations.append(row[1])
    # Plot the values and set options for the plot design
    plt.plot(years, populations)
    plt.xticks(years, rotation=270)
    plt.title(f"{city["name"]}'s Population Over 20 Years")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.tight_layout()
    # Display the plot to the user
    plt.show()

# Run the main function this file is ran directly
if __name__ == "__main__":
    main()