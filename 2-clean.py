import pandas as pd

df = pd.read_csv("Liste_Clients_Actif_2024_avec_Secteurs.csv")

n = 0    

df.drop_duplicates(subset='CODE_CLIENT', inplace=True)


for index, row in df.iterrows():
    n += 1

# Save the cleaned data
df.to_csv("CLEAN.csv", index=False)

print("Processing complete!")
print(f"Total number of rows processed: {n}")
