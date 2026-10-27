import pandas as pd
import matplotlib.pyplot as plt




# Task 1: read CSV into a DataFrame
# Read CSV file
df = pd.read_csv("Cars93_missing.csv")
#display
print(df)

# Task 2: object column -> index 
df["Make"] = df["Make"].fillna(df["Manufacturer"].fillna("Unknown") + " " + df["Model"].fillna("Unknown"))
df = df.set_index("Make")
print("\nTASK 2"); print(df.index[:5].tolist())


#  Task 3: change values by condition 
df.loc[df["Price"] > 40, "Price"] = 40                 
df.loc[df["Origin"] == "non-USA", "Origin"] = "Foreign"
print("\nTASK 3"); print("Max price now:", df["Price"].max()); print(df["Origin"].value_counts())

#  Task 4: column names + missing values 
print("\nTASK 4"); print(df.columns.tolist())
print(df.isna().sum())
print("Total missing:", df.isna().sum().sum())

# Task 5: swap 2 columns with a function, sort columns by name 
def swap_columns(data, a, b):
    cols = list(data.columns)
    i, j = cols.index(a), cols.index(b)
    cols[i], cols[j] = cols[j], cols[i]
    return data[cols]

df = swap_columns(df, "Price", "Weight")
df = df.sort_index(axis=1)
print("\nTASK 5"); print(df.columns.tolist())

#  Task 6: delete upper and lower 5% 
low, high = df["Price"].quantile([0.05, 0.95])
df_trim = df[(df["Price"] >= low) & (df["Price"] <= high)]
print("\nTASK 6"); print(f"low={low:.2f}, high={high:.2f}, rows {len(df)} -> {len(df_trim)}")

# Task 7: fill missing values with column mean 
num_cols = df.select_dtypes("number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
print("\nTASK 7"); print("Missing in numeric columns:", df[num_cols].isna().sum().sum())

# Task 8: two dicts -> two DataFrames -> merge -> append as new column 
d1 = {"id": [1, 2, 3], "name": ["Anna", "Ben", "Carl"]}
d2 = {"id": [1, 2, 3], "score": [85, 90, 78]}
df1, df2 = pd.DataFrame(d1), pd.DataFrame(d2)
merged = pd.merge(df1, df2, on="id")
df1["score"] = df2["score"]
print("\nTASK 8"); print(merged); print(df1)

# Task 9: histogram 
plt.figure()
plt.hist(df["Price"], bins=15, edgecolor="black")
plt.xlabel("Price (in $1000)"); plt.ylabel("Frequency"); plt.title("Histogram of Price")
plt.savefig("hist.png", dpi=120); plt.close()

# Task 10: correlation matrix 
corr = df.select_dtypes("number").corr(method="pearson")
print("\nTASK 10"); print(corr.round(2).iloc[:6, :6])
plt.figure(figsize=(10, 8))
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1); plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.title("Correlation matrix"); plt.tight_layout()
plt.savefig("corr.png", dpi=120); plt.close()
