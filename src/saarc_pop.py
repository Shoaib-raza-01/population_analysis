import csv
import matplotlib.pyplot as plt

SAARC_COUNTY = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]

with open('../dataset/population-estimates_csv.csv', 'r') as file:
    reader = csv.DictReader(file)
    saarc_cntry_pop = {}
    for row in reader:
        population = row.get('Population')
        country = row.get('Region')

        if country in SAARC_COUNTY:
            if country not in saarc_cntry_pop:
                saarc_cntry_pop[country] = int(float(population))
            else:
                saarc_cntry_pop[country] += int(float(population))
    # print(saarc_cntry_pop)
    plt.bar(saarc_cntry_pop.keys(), saarc_cntry_pop.values())
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.title("Population of SAARC over the years")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../images/SAARC_over_the_year.png')
    