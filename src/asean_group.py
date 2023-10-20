import csv
import matplotlib.pyplot as plt

ASEAN_COUNTRY = ["Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]

with open("../dataset/population-estimates_csv.csv", 'r') as file:
    reader = csv.DictReader(file)
    asean_pop_2004_14 = {}
    for row in reader:
        year = int(row.get('Year'))
        population = row.get('Population')
        country = row.get('Region')

        if year >= 2004 and year <= 2014:
            if country in ASEAN_COUNTRY:
                if country not in asean_pop_2004_14:
                    asean_pop_2004_14[country] = {}
                # if year not in asean_pop_2004_14[country]:
                asean_pop_2004_14[country][year] = float(population)
   
    country =list(asean_pop_2004_14.keys())
    # print(country)
    years = range(2004,2015)
    values_by_year = {}

    for year in years:
        values_by_year[year] = [asean_pop_2004_14[country][year] for country in asean_pop_2004_14]

    # print(values_by_year)
    yearList = list(values_by_year.keys())
    populationList = []
    for i,pop in values_by_year.items():
        populationList.append(list(pop))
    # print(populationList)
    colorList= ['g','r','y','b','pink','orange','indigo','brown']
    for i in range(8):
        plt.bar(0,0, label= country[i], color= colorList[i])
    offset = 0
    bar_width = 0.1
    for i in range(len(yearList)):
        for j in range(len(populationList[i])):
            plt.bar(offset, populationList[i][j], width=bar_width, color = colorList[j])
            offset += bar_width
        offset+= bar_width*2
    position = list(range(len(yearList)))
    for i in range(len(position)):
        position[i] += bar_width*2
    plt.xlabel('country')
    plt.xticks(position,yearList, rotation = 90)
    plt.ylabel('Population')
    plt.title('Population of Southeast Asian country (2004-2014)')
    plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()






    plt.savefig('../images/test.png')
    