# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Step 2: Load the World Bank population dataset
# Skip first 4 rows because they contain metadata
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)

# Step 3: Display first few rows to check the data
print("First few rows of the dataset:")
display(df.head())
# Step 4: Extract population data for a specific year (example: 2022)
df_latest = df[['Country Name', '2022']].dropna()
df_latest.columns = ['Country', 'Population']

# Step 5: Sort by population and select top 20 most populous countries
top_20 = df_latest.sort_values(by='Population', ascending=False).head(20)
# Step 6: Bar Chart - Top 20 most populous countries
plt.figure(figsize=(12, 6))
sns.barplot(data=top_20, y='Country', x='Population', palette='viridis')
plt.title("Top 20 Most Populous Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
# Step 7: Histogram - Distribution of population across countries
plt.figure(figsize=(10, 6))
sns.histplot(df_latest['Population'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Country Populations (2022)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.show()
