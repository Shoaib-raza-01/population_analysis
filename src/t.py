import matplotlib.pyplot as plt

# Data for the countries
countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand']

# Population data for the years 2004 to 2014
population_data = {
    2004: [359.523, 13063.377, 223614.649, 25174.109, 48073.707, 84678.493, 4370.04, 65002.231],
    2005: [365.158, 13270.201, 226712.73, 25659.393, 48482.614, 86274.237, 4491.042, 65425.47],
    2006: [370.25, 13474.489, 229838.202, 26143.566, 48846.474, 87809.419, 4611.901, 65824.164],
    2007: [374.864, 13676.693, 232989.141, 26625.845, 49171.586, 89293.49, 4732.528, 66195.615],
    2008: [379.252, 13880.509, 236159.276, 27111.069, 49479.752, 90751.864, 4851.109, 66545.76],
    2009: [383.772, 14090.208, 239340.478, 27605.383, 49800.69, 92220.879, 4965.518, 66881.867],
    2010: [388.662, 14308.74, 242524.123, 28112.289, 50155.896, 93726.624, 5074.252, 67208.808],
    2011: [394.013, 14537.886, 245707.511, 28635.128, 50553.031, 95277.94, 5176.017, 67530.13],
    2012: [399.748, 14776.866, 248883.232, 29170.456, 50986.514, 96866.642, 5270.958, 67843.979],
    2013: [405.716, 15022.692, 252032.263, 29706.724, 51448.196, 98481.032, 5360.837, 68143.065],
    2014: [411.704, 15270.79, 255131.116, 30228.017, 51924.182, 100102.249, 5448.342, 68416.772]
}

# Transpose the population data for plotting
years = list(population_data.keys())
populations = [population_data[year] for year in years]

# Create the grouped bar chart
num_years = len(years)
bar_width = 0.15
bar_positions = range(len(countries))

for i in range(num_years):
    plt.bar(
        [pos + i * bar_width - (bar_width * num_years / 2) for pos in bar_positions],
        populations[i],
        width=bar_width,
        label=str(years[i])
    )
    

plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('Population of Southeast Asian Countries (2004-2014)')
plt.xticks([pos - (bar_width * num_years / 2) + bar_width * (num_years / 2) for pos in bar_positions], countries, rotation=45, ha="right")
plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
# plt.show()

plt.savefig('../images/t.png')
