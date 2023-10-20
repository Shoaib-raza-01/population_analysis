import csv
import matplotlib.pyplot as plt

ASEAN_COUNTRY = ["Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]

with open("../dataset/population-estimates_csv.csv", 'r') as file:
    reader = csv.DictReader(file)
    asean_pop_2014 = {}
    for row in reader:
        year = row.get('Year')
        population = row.get('Population')
        country = row.get('Region')

        if year == '2014':
            if country in ASEAN_COUNTRY:
                asean_pop_2014[country] = int(float(population))
        # print(row)
    plt.bar(asean_pop_2014.keys(), asean_pop_2014.values())
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.title("Population of ASEAN country in 2014")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../images/asean_2014.png')