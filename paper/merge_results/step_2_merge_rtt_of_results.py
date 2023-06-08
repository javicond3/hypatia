import pandas as pd


of_path = '../of/prepared_rtt_of.csv'
satellite_path ='../ns3_experiments/a_b/rtt_merged.csv'
merged_satellite_of_path = './rtt_merged_of_satellite.csv'

def mergeFiles():
    df_satellite = pd.read_csv(satellite_path)
    df_of = pd.read_csv(of_path)

    merged_df = pd.merge(df_satellite, df_of, on=['origin_name', 'destination_name'], how='left')
    merged_df.to_csv(merged_satellite_of_path, index=False)


mergeFiles()

print("Finished")