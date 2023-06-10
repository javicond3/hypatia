import os
import csv
import re
import pandas as pd


folder_path = '../satgenpy_analysis/data'
csv_path = '../satgenpy_analysis/satellites.csv'
merged_csv_path ='../satgenpy_analysis/satellites_merged.csv'


# Get a list of all items in the folder
items = os.listdir(folder_path)

header = ["constellation", "origin", "destination", "origin_name", "destination_name", "satellites"]


# Filter out only the directories
folder_names = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]

def calculate_mean_satellites(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        total_satellites = 0
        total_lines = 0

        for line in lines:
            line = line.strip()
            
            if ('-') in line:
                satellites = len(re.findall('-', line)) - 1
                total_satellites += satellites
                total_lines += 1

        mean_satellites = total_satellites / total_lines if total_lines > 0 else 0

        return mean_satellites
    
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
    

def getFolderValues(folder_name):
    values =  folder_name.split("_")
    return [values[0]]

def getFileValues(file_name):
    values =  file_name.split("_")
    return [values[2], values[4].split(".txt")[0]]


with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for folder_name in folder_names:
        if folder_name != 'command_logs':
            folder_path_2 = folder_path+"/"+folder_name+'/data'
            file_names = [item for item in os.listdir(folder_path_2) if os.path.isfile(os.path.join(folder_path_2, item))]
            for file_name in file_names:
                if '_path_' in file_name:
                    satellites = [calculate_mean_satellites(folder_path_2 + "/" + file_name)]
                    folder_values = getFolderValues(folder_name)
                    file_values = getFileValues(file_name)
                    cityNames = getCityName(folder_values[0], file_values[0], file_values[1])
                    row = folder_values + file_values + cityNames + satellites
                    writer.writerows([row])


def mergeConstellations():
    df = pd.read_csv(csv_path)

    constellations = df['constellation'].unique()

    constellation_dfs = {}

    for constellation in constellations:
        filtered_df = df[df['constellation'] == constellation]
        
        new_columns = [
            column + '_' + constellation if column not in ['origin_name', 'destination_name'] else column
            for column in filtered_df.columns
        ]
        

        filtered_df.columns = new_columns
        
        constellation_dfs[constellation] = filtered_df


    merged_df = pd.merge(constellation_dfs['telesat'], constellation_dfs['kuiper'], on=['origin_name', 'destination_name'], how='outer')
    merged_df = pd.merge(merged_df, constellation_dfs['starlink'], on=['origin_name', 'destination_name'], how='outer')
    new_order = ['origin_name', 'destination_name'] + [col for col in merged_df.columns if col not in ['origin_name', 'destination_name']]
    merged_df = merged_df[new_order]
    merged_df_resultant = merged_df[['origin_name', 'destination_name', 'satellites_telesat', 'satellites_kuiper', 'satellites_starlink']]
    merged_df_resultant.to_csv(merged_csv_path, index=False)


mergeConstellations()
print("Results generated")
