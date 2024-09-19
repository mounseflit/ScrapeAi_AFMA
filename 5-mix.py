import pandas as pd

df1 = pd.read_csv("Liste_Clients_Actif_2024_avec_Secteurs.csv")

df2 = pd.read_csv("RESULTS.csv")

df2 = df2._append(df1[~df1['NOM_CLIENT'].isin(df2['NOM_CLIENT'])])

df2.reset_index(drop=True, inplace=True)

df2.to_csv("MIXED.csv", index=False)

print("Mixing complete!")
