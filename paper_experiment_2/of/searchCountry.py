import pandas as pd
import pprint

cities = [
"Frankfurt",
"Munich",
"Amsterdam",
"London",
"Rome",
"Barcelona",
"Venice",
"Helsinki",
"Moscow"
]

cities_dict = {
"Frankfurt": {"count": 0, "cities":[]},
"Munich": {"count": 0, "cities":[]},
"Amsterdam": {"count": 0, "cities":[]},
"London": {"count": 0, "cities":[]},
"Rome": {"count": 0, "cities":[]},
"Barcelona": {"count": 0, "cities":[]},
"Venice": {"count": 0, "cities":[]},
"Helsinki": {"count": 0, "cities":[]},
"Moscow": {"count": 0, "cities":[]},
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