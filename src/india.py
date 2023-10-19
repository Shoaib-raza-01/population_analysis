import csv
import matplotlib.pyplot as plt

def execute():
    with open('../dataset/population-estimates_csv.csv', 'r') as file:
        reader = csv.DictReader(file)
        india_over_the_year = {}

        for row in reader:
            year = row.get('Year')
            population = row.get('Population')
            country = row.get('Region')

            if country == 'India':
                if year not in india_over_the_year:
                    india_over_the_year[year] = population
        # print(india_over_the_year)
        plt.bar(india_over_the_year.keys(), india_over_the_year.values())
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population of India over the years")
        plt.xticks(rotation=90)
        plt.savefig('../images/india_over_the_year.png')

execute()
