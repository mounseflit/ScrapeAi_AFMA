
import pandas as pd

df = pd.read_csv("Liste_Clients_Actif_2024_avec_Secteurs.csv")

n = 0    

for index, row in df.iterrows():
    if row['Secteur Activité'] == "Non classifié" or row['Sous-secteur'] == "Non classifié" or row['Sous-sous-secteur'] == "Non classifié":
        n += 1

print("Processing complete!")

print(f"Total number of rows Non classifié: {n}")
print(f"Total number of rows classifié: {16825-n}")
print(f"Total number of rows: {16825}")
print(f"Time to processe : {n*3/60/60} hours")
