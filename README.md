# Pandas-HandsOn
Learning and practicing data analysis, cleaning, and transformation with Pandas.


# Pandas Practice Repository

A collection of Pandas examples, exercises, and mini-projects created while learning data analysis with Python. This repository covers essential Pandas concepts such as data loading, cleaning, filtering, aggregation, transformation, and visualization preparation.

## 🎯 Aim

The goal of this repository is to learn and practice the Pandas library for efficient data manipulation and analysis. It serves as a personal reference and learning resource for data science and data analytics.

## 📚 Topics Covered

- Introduction to Pandas
- Series and DataFrame
- Reading and Writing Files (CSV, Excel, JSON)
- Data Inspection and Exploration
- Data Cleaning
- Handling Missing Values
- Data Filtering and Selection
- Sorting Data
- GroupBy Operations
- Data Aggregation
- Merging and Joining DataFrames
- Concatenation
- Pivot Tables
- Date and Time Operations
- Data Visualization Preparation
- Real-World Dataset Analysis

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

## 📂 Repository Structure
PANDAS/
│
├── basics/
├── data-cleaning/
├── filtering/
├── groupby/
├── merging/
├── pivot-tables/
├── datasets/
├── mini-projects/
└── README.md

💡 Example
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)

print(df)

Output:
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   35
