import pandas as pd


merged_satellite_of_path = './rtt_merged_of_satellite.csv'
merged_number_satellite_path ='../satgenpy_analysis/satellites_merged.csv'
merged_satellite_of_number_satellite_path = './rtt_merged_of_satellite_number_satellite.csv'


def mergeFiles():
    df_satellite = pd.read_csv(merged_satellite_of_path)
    df_number_satellite = pd.read_csv(merged_number_satellite_path)

    merged_df = pd.merge(df_satellite, df_number_satellite, on=['origin_name', 'destination_name'], how='left')
    merged_df.to_csv(merged_satellite_of_number_satellite_path, index=False)


mergeFiles()

print("Finished")