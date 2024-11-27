import pandas as pd
import matplotlib.pyplot as plt

# Skaityti CSV failą
df = pd.read_csv('MadridPolution2001-2022.csv')

# Vizualizuoti
plt.plot(df['Time'], df['BEN'], marker='o', label='BEN')
plt.title('Temperatūros pokytis')
plt.xlabel('Laikas')
plt.ylabel('Temperatūra')
plt.legend()
plt.grid()
plt.show()
