import os
import csv
import re


folder_path = './runs'
csv_path = './runs/rtt.csv'

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
    if constellation == "telesat":
        origin_id = int(origin) - 351
        dest_id = int(dest) - 351
    else:
        print("Error in constellation")

    city_names = {
        0: "Madrid",
        1: "Barcelona",
        2: "Ankara",
        3: "Los-Angeles",
        4: "New-York",
        5: "Mexico-City",
        6: "Buenos-Aires",
        7: "Nairobi",
        8: "Beijing",
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
        file_name = './runs/'+folder_name+'/logs_ns3/pingmesh.txt'
        folder_name_values = getFolderValues(folder_name)
        folder_file_values = getFileValues(file_name)
        cityNames = getCityName(folder_name_values[0], folder_name_values[3], folder_name_values[4])
        folder_file_values[0] = cityNames[0]
        folder_file_values[1] = cityNames[1]
        row = folder_name_values + folder_file_values
        writer.writerows([row])

print("Results generated")




