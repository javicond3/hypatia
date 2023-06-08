import pandas as pd
import pprint

cities = [
"Madrid",
"Barcelona",
"Riyadh",
"Los-Angeles",
"New-York",
"Mexico-City",
"Bogota",
"Cairo",
"Tokyo",
"Sidney",
]

cities_dict = {
"Madrid": {"count": 0, "cities":[]},
"Barcelona": {"count": 0, "cities":[]},
"Riyadh": {"count": 0, "cities":[]},
"Los-Angeles": {"count": 0, "cities":[]},
"New-York": {"count": 0, "cities":[]},
"Mexico-City": {"count": 0, "cities":[]},
"Bogota": {"count": 0, "cities":[]},
"Cairo": {"count": 0, "cities":[]},
"Tokyo": {"count": 0, "cities":[]},
"Sidney": {"count": 0, "cities":[]},
}

csv_path = './prepared_rtt_of.csv'

df = pd.read_csv(csv_path)
count = 0

for i in cities:
    for j in cities:
        if i != j:
            if df[(df['origin_name'] == i) & (df['destination_name'] == j)].empty:
                cities_dict[i]["count"] += 1
                cities_dict[i]["cities"].append(j)
                count += 1
            else:
                None


pprint.pprint(cities_dict)
print("="*10)
print(count)
