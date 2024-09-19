import pandas as pd

df = pd.read_csv("CLEAN.csv")

n = 0    


for index, row in df.iterrows():
    n += 1

df.to_csv("RESULTS.csv", index=False)

print("Processing complete!")
print(f"Total number of rows processed: {n}")
