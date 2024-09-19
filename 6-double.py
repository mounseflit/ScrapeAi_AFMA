import pandas as pd

df = pd.read_csv("MIXED.csv")

n = 0    

df.drop_duplicates(subset='CODE_CLIENT', inplace=True)

for index, row in df.iterrows():
    n += 1

df.to_csv("FINAL.csv", index=False)

print("Processing complete!")
print(f"Total number of rows processed: {n}")
