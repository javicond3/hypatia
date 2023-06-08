import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('raw_rtt_of.csv')

# Reemplazar celdas vacías con el contenido de la celda anterior si no está vacía
df = df.fillna(method='ffill')

# Guardar el resultado en un nuevo archivo CSV
df.to_csv('prepared_rtt_of.csv', index=False)
print("Finished")
