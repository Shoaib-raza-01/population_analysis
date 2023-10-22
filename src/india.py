"""csv Matplotlib"""
import csv
import matplotlib.pyplot as plt

UN_POPULATION = "../dataset/population-estimates_csv.csv"


def plot(india_over_the_year):
    """ploting graph"""
    plt.bar(india_over_the_year.keys(), india_over_the_year.values())
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population of India over the years")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../images/india_over_the_year.png')


def execute():
    """creating the data for plot function"""
    india_over_the_year = {}
    with open(UN_POPULATION, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = row.get('Year')
            population = row.get('Population')
            country = row.get('Region')

            if country == 'India':
                if year not in india_over_the_year:
                    india_over_the_year[year] = int(float(population))
        # print(india_over_the_year)
    plot(india_over_the_year)


execute()
