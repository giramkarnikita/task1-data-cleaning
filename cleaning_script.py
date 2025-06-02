import pandas as pd

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Drop duplicates
df = df.drop_duplicates()

# Standardize text values
df['gender'] = df['gender'].str.lower().str.strip()
df['race/ethnicity'] = df['race/ethnicity'].str.upper().str.strip()
df['parental level of education'] = df['parental level of education'].str.title().str.strip()
df['lunch'] = df['lunch'].str.lower().str.strip()
df['test preparation course'] = df['test preparation course'].str.lower().str.strip()

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert data types
df['math_score'] = df['math_score'].astype(int)
df['reading_score'] = df['reading_score'].astype(int)
df['writing_score'] = df['writing_score'].astype(int)

# Save cleaned data
df.to_csv("StudentsPerformance_Cleaned.csv", index=False)
