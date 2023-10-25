import pandas as pd
import pprint
import sys
sys.path.append('../satellite_networks_state/input_data')

from experimentCities import Cities

cities = Cities.generateCitiesArray()

cities_dict = Cities.generateCitiesDictCount()

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
