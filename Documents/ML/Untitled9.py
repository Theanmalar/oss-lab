import pandas as pd

# 1. Load Data
# You can load a CSV, Excel, or any other supported file format.
df = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with your actual file path

# 2. Data Overview
print("First 5 rows of the dataset:")
print(df.head())  # Shows the first 5 rows

print("\nData info (data types, missing values):")
print(df.info())  # Shows a summary of the dataset

# 3. Handling Missing Values
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())  # Counts missing values per column

# Fill missing values or drop rows/columns with missing values
# Example: Fill missing values with the mean or mode
df['column_name'] = df['column_name'].fillna(df['column_name'].mean())  # Replace with mean
# OR: Drop rows with missing values
# df.dropna(inplace=True)

# 4. Data Filtering and Selection
# Example: Select data based on a condition
filtered_df = df[df['age'] > 30]  # Filter rows where 'age' is greater than 30
print("\nFiltered Data:")
print(filtered_df)

# 5. Grouping Data
# Example: Group by a column and aggregate
grouped_df = df.groupby('category')['sales'].sum()  # Group by 'category' and sum 'sales'
print("\nGrouped Data (Sum of sales by category):")
print(grouped_df)

# 6. Data Transformation
# Example: Add a new column based on existing data
df['total_sales'] = df['price'] * df['quantity']  # Create a new column 'total_sales'

# Example: Apply a function to each row
df['discounted_price'] = df['price'].apply(lambda x: x * 0.9)  # Apply a 10% discount

# 7. Sorting Data
# Example: Sort data by a column
sorted_df = df.sort_values(by='total_sales', ascending=False)  # Sort by 'total_sales' descending
print("\nSorted Data:")
print(sorted_df.head())  # Show the first few rows after sorting

# 8. Export Data
# Save the cleaned or processed data to a new file
df.to_csv('cleaned_data.csv', index=False)  # Save the cleaned data to a new CSV file

# 9. Data Visualization (Optional)
import matplotlib.pyplot as plt

# Example: Plot a simple bar chart
df['category'].value_counts().plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()





