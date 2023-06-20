import os
import csv
import re
import pandas as pd


folder_path = '../ns3_experiments/a_b/runs'
csv_path = '../ns3_experiments/a_b/rtt.csv'
merged_csv_path ='../ns3_experiments/a_b/rtt_merged.csv'

# Get a list of all items in the folder
items = os.listdir(folder_path)

header = ["constellation", "height", "type", "origin", 
          "destination", "origin_name", "destination_name", "Mean latency there", 
          "Mean latency back", "Min. RTT", "Mean RTT", "Max. RTT", 
          "Smp.std. RTT", "Reply arrival"]


# Filter out only the directories
folder_names = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]

def getCityName(constellation, origin, dest):
    origin_id = -1
    origin_name = "Unknown"
    dest_id = -1
    dest_name = "Unknown"
    count = 0
    if constellation == "kuiper":
        count = 1156
    elif constellation == "starlink":
        count = 1584
    elif constellation == "telesat":
        count = 351
    else:
        print("Error in constellation")
    origin_id = int(origin) - count
    dest_id = int(dest) - count

    city_names = {
        0: "Madrid",
        1: "Barcelona",
        2: "Riyadh",
        3: "Los-Angeles",
        4: "New-York",
        5: "Mexico-City",
        6: "Bogota",
        7: "Cairo",
        8: "Tokyo",
        9: "Sidney"
    }
    

    origin_name = city_names.get(origin_id, "Unknown")
    dest_name = city_names.get(dest_id, "Unknown")

    return [origin_name, dest_name]
    

def getFileValues(file_name):

    with open(file_name, "r") as archivo:
        text = archivo.read()


    pattern = r'(\d+)\s+(\d+)\s+([\d.]+\s\w+)\s+([\d.]+\s\w+)\s+([\d.]+\s\w+)\s+([\d.]+\s\w+)\s+([\d.]+\s\w+)\s+([\d.]+\s\w+)\s+([\d./]+\s\(\d+%\))'

    values = re.search(pattern, text)
    return [values.group(1),
            values.group(2),
            values.group(3),
            values.group(4),
            values.group(5),
            values.group(6),
            values.group(7),
            values.group(8),
            values.group(9)
            ]

def getFolderValues(folder_name):
    values =  folder_name.split("_")
    return [values[0], values[1], values[2], values[3], values[5]]



with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for folder_name in folder_names:
        file_name = folder_path+"/"+folder_name+'/logs_ns3/pingmesh.txt'
        folder_name_values = getFolderValues(folder_name)
        folder_file_values = getFileValues(file_name)
        cityNames = getCityName(folder_name_values[0], folder_name_values[3], folder_name_values[4])
        folder_file_values[0] = cityNames[0]
        folder_file_values[1] = cityNames[1]
        row = folder_name_values + folder_file_values
        writer.writerows([row])


def mergeConstellations():
    df = pd.read_csv(csv_path)

    constellations = df['constellation'].unique()

    constellation_dfs = {}

    for constellation in constellations:
        filtered_df = df[df['constellation'] == constellation]
        
        new_columns = [
            column + '_' + constellation if column not in ['origin_name', 'destination_name', 'type'] else column
            for column in filtered_df.columns
        ]
        

        filtered_df.columns = new_columns
        
        constellation_dfs[constellation] = filtered_df


    merged_df = pd.merge(constellation_dfs['telesat'], constellation_dfs['kuiper'], on=['origin_name', 'destination_name', 'type'], how='outer')
    merged_df = pd.merge(merged_df, constellation_dfs['starlink'], on=['origin_name', 'destination_name', 'type'], how='outer')
    new_order = ['origin_name', 'destination_name', 'type'] + [col for col in merged_df.columns if col not in ['origin_name', 'destination_name', 'type']]
    merged_df = merged_df[new_order]

    merged_df.to_csv(merged_csv_path, index=False)


mergeConstellations()
print("Results generated")
