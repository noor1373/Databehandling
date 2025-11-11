import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1
cities_and_population = pd.DataFrame({
    'Kommun':['Malmö', 'Stockholm', 'Uppsala', 'Göteborg'],
    'Population':[347949, 975551, 233839, 583056]
})

# a) Use your DataFrame to print out all the cities

cities = [cities_and_population["Kommun"]]

print(f"All the cities:\n {cities}\n")

# b) Select only the row which contains Göteborg.
# Do this by using the name Göteborg.

city = [cities_and_population["Kommun"] == "Göteborg"]

print(city)

# c) Sort the cities by population from largest to smallest

sorted_cities = cities_and_population.sort_values(by="Population", ascending=False, ignore_index=True)

print(f"Sorted cities by population:\n {sorted_cities}\n")

# d) Filter out the three largest cities

cities_largest3 = sorted_cities.iloc[:3]

print(f"The three largest cities:\n {cities_largest3}\n")

# e) The whole population in Sweden 2020 is 10379295
# Use this number to create a new column in your sorted DataFrame named: Population (%).
# This column should be filled with percentage of the Swedish population for each city.

cities_and_population['Popolation (%)'] = (cities_and_population['Population'] / 10379295 * 100).round(1)

print(f"The whole population in sweden 2020 is:\n {cities_and_population}\n")

# 2. Cities in Sweden - real dataset
# a) Read in the tab "Totalt" into a DataFrame

df = pd.read_excel(r"C:\Users\noorq\Desktop\Repository AI25\Databehandling\AI25-Databehandling\Data\komtopp50_2020.xlsx", sheet_name="Totalt", header=[6])

df.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]

sorted_cities = df.sort_values(by="Folkmängd 2020", ascending=False, ignore_index=True)

print(f"Cities sorted by population:\n {sorted_cities}\n")

cities_smallest5 = df.sort_values(by="Rang 2020", ascending=False, ignore_index=True).head(5)

print(f"The five smallest cities:\n {cities_smallest5}\n")

print(f"Sweden's population in 2019:\n {df["Folkmängd 2019"].sum()}\n")
print(f"Sweden's population in 2020:\n {df["Folkmängd 2020"].sum()}\n")


df_largest = sorted_cities.head(5)
df_smallest =sorted_cities.tail(5)

fig, axes = plt.subplots(1,2, dpi=100, figsize=(6,3))
titles = ["Sveriges 5 största kommun 2020", "Sveriges 5 minsta kommun 2020"]
dataframes = [df_largest, df_smallest]

for i, (data, title) in enumerate(zip(dataframes,titles)):
    sns.barplot(
        data=data,
        x="Kommun", 
        y="Folkmängd 2020",
        ax= axes[i], 
        hue="Kommun"
    )
    axes[i].set(title=title)

plt.show()

# 3. Cities in Sweden - gender

def komtopp50(sheet=1):
    df.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]
    return pd.read_excel(r"C:\Users\noorq\Desktop\Repository AI25\Databehandling\AI25-Databehandling\Data\komtopp50_2020.xlsx", names=df.columns, sheet_name=sheet, skiprows=6)

female, male = komtopp50(2), komtopp50(3)
female["Kön"], male["Kön"] = "Kvinna", "Man"

print(f"Male:\n {male.head()}\n")
print(f"Female:\n {female.head()}\n")


