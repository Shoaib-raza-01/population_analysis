"""importing modules"""
import csv
import matplotlib.pyplot as plt

ASEAN_COUNTRY = [
    "Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia",
    "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]
UN_POPULATION = "../dataset/population-estimates_csv.csv"


def plot(asean_pop_14):
    """ploting the graph"""
    plt.bar(asean_pop_14.keys(), asean_pop_14.values())
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.title("Population of ASEAN country in 2014")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../images/asean_2014.png')


def execute():
    """creating the data for plotting"""
    asean_pop_2014 = {}
    with open(UN_POPULATION, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = row.get('Year')
            population = row.get('Population')
            country = row.get('Region')

            if year == '2014':
                if country in ASEAN_COUNTRY:
                    asean_pop_2014[country] = int(float(population))
        # print(row)
    plot(asean_pop_2014)


execute()
