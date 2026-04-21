import sqlite3, random
from math import floor
import matplotlib.pyplot as plt


def main():
    conn = sqlite3.connect("population_ZK.db")
    cursor = conn.cursor()
    query = ("CREATE TABLE IF NOT EXISTS population (city TEXT, year INTEGER, "
             "population INTEGER)")
    cursor.execute(query)
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

    # for city in CITIES:
    #     insertCity(cursor, city["name"], city["year"], city["population"])
    # conn.commit()

    # allCities = []
    # cursor.execute("SELECT city, year, population FROM population WHERE year = 2025 ORDER BY city")
    # for city in cursor.fetchall():
    #     allCities.append({"name": city[0], "year": city[1], "population": city[2]})
    #
    # for city in allCities:
    #     simulatePopulation(cursor, city)

    while True:
        for index, city in enumerate(CITIES):
            print(f"{index + 1}. {city["name"]}")
        requestedCity = input("Please pick a city from above (#): ")
        try:
            requestedCity = int(requestedCity)
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            if requestedCity not in range(1, len(CITIES) + 1):
                print("Please enter a valid option from above.")
                continue
            generatePlot(cursor, CITIES[requestedCity-1])
            break

    conn.commit()
    conn.close()

def insertCity(cursor, city, year, population):
    query = f"INSERT INTO population VALUES ('{city}', {year}, {population})"
    cursor.execute(query)

def simulatePopulation(cursor, city):
    for i in range(1,21):
        populationChange = random.randint(-3, 3)
        populationChange = 1 + (populationChange / 100)
        cursor.execute(f"SELECT population FROM population WHERE city='{city["name"]}' ORDER BY year DESC LIMIT 1")
        output = cursor.fetchone()
        newPopulation = floor(output[0] * populationChange)
        cursor.execute(f"INSERT INTO population VALUES ('{city["name"]}', {city["year"] + i}, {newPopulation})")

def generatePlot(cursor, city):
    cursor.execute(f"SELECT year, population FROM population WHERE city='{city["name"]}' ORDER BY year")
    output = cursor.fetchall()
    years = []
    populations = []
    for row in output:
        years.append(row[0])
        populations.append(row[1])
    plt.plot(years, populations)
    plt.xticks(years, rotation=270)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()


if __name__ == "__main__":
    main()