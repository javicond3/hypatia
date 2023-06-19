import pandas as pd
import pprint

cities = [
"Cairo",
"TelAviv",
"Jerusalem",
"Limassol",
"Beirut",
"Ankara",
"Izmir",
"Athens",
"Tunis",
]

cities_dict = {
"Cairo": {"count": 0, "cities":[]},
"TelAviv": {"count": 0, "cities":[]},
"Jerusalem": {"count": 0, "cities":[]},
"Limassol": {"count": 0, "cities":[]},
"Beirut": {"count": 0, "cities":[]},
"Ankara": {"count": 0, "cities":[]},
"Izmir": {"count": 0, "cities":[]},
"Athens": {"count": 0, "cities":[]},
"Tunis": {"count": 0, "cities":[]},
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
