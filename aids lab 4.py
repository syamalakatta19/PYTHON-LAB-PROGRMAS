import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Arun",
             "Kiran", "Anu", "Ravi", "Meena", "Vijay"],

    "Age": [20, 21, 19, 20, 22, 21, 20, 19, 21, 22],

    "Study_Hours": [2, 4, 5, 3, 6, 7, 4, 2, 6, 5],

    "Attendance": [75, 85, 90, 80, 95, 92, 88, 70, 96, 89],

    "Marks": [55, 68, 82, 60, 90, 95, 75, 50, 92, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Student Performance Dataset:")
print(df)

# First 5 records
print("\nFirst 5 Records:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Mean
print("\nMean:")
print(df.select_dtypes("number").mean())

# Median
print("\nMedian:")
print(df.select_dtypes("number").median())

# Standard deviation
print("\nStandard Deviation:")
print(df.select_dtypes("number").std())

# Scatter plot: Study Hours vs Marks
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks"
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Scatter plot: Attendance vs Marks
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Marks"
)

plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.show()

# Histogram of Marks
plt.hist(df["Marks"], bins=5)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# Boxplot of Marks
sns.boxplot(y=df["Marks"])

plt.title("Marks Distribution")
plt.ylabel("Marks")
plt.show()