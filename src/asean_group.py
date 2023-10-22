"""importing"""
import csv
import matplotlib.pyplot as plt

ASEAN_COUNTRY = [
    "Brunei Darussalam", "Cambodia", "Indonesia", "Laos",
    "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]
UN_POPULATION = "../dataset/population-estimates_csv.csv"


def plot(country, year_list, population_list):
    """ploting the graph"""
    color_list = ['g', 'r', 'y', 'b', 'pink', 'orange', 'indigo', 'brown']
    for i in range(8):
        plt.bar(0, 0, label=country[i], color=color_list[i])
    offset = 0
    bar_width = 0.1
    for i in range(len(year_list)):
        for j in range(len(population_list[i])):
            plt.bar(offset, population_list[i][j],
                    width=bar_width, color=color_list[j])
            offset += bar_width
        offset += bar_width * 2
    position = list(range(len(year_list)))
    for i in range(len(position)):
        position[i] += bar_width*2
    plt.xlabel('country')
    plt.xticks(position, year_list, rotation=90)
    plt.ylabel('Population')
    plt.title('Population of Southeast Asian country (2004-2014)')
    plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig('../images/group_chart.png')
    # plt.savefig('../images/plot2.png')


def execute():
    """execute funtion to create the data"""
    with open(UN_POPULATION, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        asean_pop_2004_14 = {}
        for row in reader:
            year = int(row.get('Year'))
            population = row.get('Population')
            country = row.get('Region')

            if 2004 <= year <= 2014:
                if country in ASEAN_COUNTRY:
                    if country not in asean_pop_2004_14:
                        asean_pop_2004_14[country] = {}
                    asean_pop_2004_14[country][year] = float(population)

        country = list(asean_pop_2004_14.keys())
        years = range(2004, 2015)
        values_by_year = {}

        for year in years:
            values_by_year[year] = [
                asean_pop_2004_14[country][year]
                for country in asean_pop_2004_14]

        year_list = list(values_by_year.keys())
        population_list = []
        for i, pop in values_by_year.items():
            population_list.append(list(pop))
        plot(country, year_list, population_list)


execute()
