# -*- coding: utf-8 -*-
"""Welcome to Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

# Specify the encoding when reading the CSV file
df = pd.read_csv('EXCEL2.csv', encoding='latin-1')  # Try 'latin-1' or other encodings if it still fails

print(df.isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt

# Load data, specifying the encoding as 'latin-1'
df = pd.read_csv('EXCEL2.csv', encoding='latin-1')

# Convert column names to handle extra whitespaces if needed
df.columns = df.columns.str.strip()

# --- Pie Chart: Solar Power vs. Other Energy Consumption ---
total_solar = df['Solar Power (kWh)'].sum()
total_consumption = df['Energy Consumption (kWh)'].sum()
total_other = total_consumption - total_solar

plt.figure(figsize=(6,6))
plt.pie(
    [total_solar, total_other],
    labels=['Solar Power', 'Other Sources'],
    autopct='%1.1f%%',
    colors=['gold', 'skyblue'],
    startangle=140
)
plt.title('Energy Source Distribution (Total)')
plt.show()

# --- Bar Chart: Actual vs. Forecasted vs. Predicted Energy Consumption ---
plt.figure(figsize=(12,6))
x = df['Hour of Day']

plt.bar(x, df['Energy Consumption (kWh)'], label='Actual', width=0.25, align='center')
plt.bar(x, df['Forecasted Energy Consumption (kWh)'], label='Forecasted', width=0.25, align='edge')
plt.bar(x, df['Model Prediction (kWh)'], label='Predicted', width=0.25, align='edge', alpha=0.7)

plt.xlabel('Hour of Day')
plt.ylabel('Energy (kWh)')
plt.title('Actual vs Forecasted vs Predicted Energy Consumption')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset, explicitly specifying the encoding as 'latin-1'
df = pd.read_csv('EXCEL2.csv', encoding='latin-1')
df.columns = df.columns.str.strip()  # Clean up column headers

# --- Histogram: Distribution of Energy Consumption ---
plt.figure(figsize=(8,5))
plt.hist(df['Energy Consumption (kWh)'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Energy Consumption')
plt.xlabel('Energy Consumption (kWh)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# --- Flow Chart: Line Plot of Energy Metrics over Time ---
plt.figure(figsize=(12,6))
x = df['Hour of Day']

plt.plot(x, df['Energy Consumption (kWh)'], label='Actual', marker='o')
plt.plot(x, df['Forecasted Energy Consumption (kWh)'], label='Forecasted', linestyle='--', marker='x')
plt.plot(x, df['Model Prediction (kWh)'], label='Predicted', linestyle='-.', marker='s')

plt.title('Energy Consumption Flow Over Time')
plt.xlabel('Hour of Day')
plt.ylabel('Energy (kWh)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()