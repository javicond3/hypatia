import pandas as pd

# Lee el archivo CSV
df = pd.read_csv("merged_of_satellite_satellite_number.csv")

# Elimina las unidades "ms" en las columnas que contengan "ms"
df.replace(" ms", "", regex=True, inplace=True)
df.replace("Madrid", "Mad", regex=True, inplace=True)
df.replace("Barcelona", "Bar", regex=True, inplace=True)
df.replace("Riyadh", "Riy", regex=True, inplace=True)
df.replace("Los-Angeles", "LA", regex=True, inplace=True)
df.replace("New-York", "NY", regex=True, inplace=True)
df.replace("Mexico-City", "Mx", regex=True, inplace=True)
df.replace("Bogota", "Bog", regex=True, inplace=True)
df.replace("Cairo", "Cai", regex=True, inplace=True)
df.replace("Tokyo", "Tok", regex=True, inplace=True)
df.replace("Sidney", "Syd", regex=True, inplace=True)

# Guarda el DataFrame modificado en un nuevo archivo CSV
df.to_csv("merged_of_satellite_satellite_number_clean.csv", index=False)
