import pandas as pd

# Skaityti CSV failą
file_path = "MadridPolution2001-2022.csv"
data = pd.read_csv(file_path)

# Pateikti pagrindinę informaciją apie duomenis
print(data.head())  # Pirmi 5 įrašai
print(data.info())  # Informacija apie stulpelius
