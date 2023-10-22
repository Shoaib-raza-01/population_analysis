"""import ,odules"""
import csv
import matplotlib.pyplot as plt

SAARC_COUNTY = ["Afghanistan", "Bangladesh", "Bhutan",
                "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]
UN_POPULATION = "../dataset/population-estimates_csv.csv"


def plot(saarc_cntry_pop):
    """ploting graph"""
    plt.bar(saarc_cntry_pop.keys(), saarc_cntry_pop.values())
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.title("Population of SAARC over the years")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('../images/SAARC_over_the_year.png')
    # plt.savefig('../images/plot2.png')


def execute():
    """creatimh the data for ploting graph"""
    saarc_cntry_pop = {}
    with open(UN_POPULATION, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            population = row.get('Population')
            country = row.get('Region')

            if country in SAARC_COUNTY:
                if country not in saarc_cntry_pop:
                    saarc_cntry_pop[country] = int(float(population))
                else:
                    saarc_cntry_pop[country] += int(float(population))
    # print(saarc_cntry_pop)
    plot(saarc_cntry_pop)


execute()
