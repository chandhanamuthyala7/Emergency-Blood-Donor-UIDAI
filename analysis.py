import pandas as pd

# Load UIDAI district-level dataset
df = pd.read_csv("data/uidai_data.csv")

# Display dataset structure
print(df.columns)

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Calculate total population count per record
df['total_population'] = (
    df['age_0_5'] +
    df['age_5_17'] +
    df['age_18_greater']
)

# District-wise aggregation
district_summary = df.groupby(['state', 'district'])[
    ['age_0_5', 'age_5_17', 'age_18_greater', 'total_population']
].sum().reset_index()

print(district_summary.head())
