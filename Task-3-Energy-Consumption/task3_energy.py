import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(
    "household_power_consumption.txt",
    sep=";",
    low_memory=False
)

# Convert Date and Time into a single datetime column
data["Datetime"] = pd.to_datetime(
    data["Date"] + " " + data["Time"],
    format="%d/%m/%Y %H:%M:%S",
    errors="coerce"
)

# Convert Global Active Power to numeric
data["Global_active_power"] = pd.to_numeric(
    data["Global_active_power"],
    errors="coerce"
)

# Remove missing values
data = data.dropna(subset=["Datetime", "Global_active_power"])

# Use only first 1000 rows for faster plotting
sample = data.head(1000)

# Line Plot
plt.figure(figsize=(10,5))
plt.plot(sample["Datetime"], sample["Global_active_power"])
plt.title("Global Active Power Over Time")
plt.xlabel("Time")
plt.ylabel("Global Active Power (kW)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(sample["Global_active_power"], bins=20)
plt.title("Distribution of Global Active Power")
plt.xlabel("Global Active Power")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(sample.index, sample["Global_active_power"])
plt.title("Global Active Power Scatter Plot")
plt.xlabel("Sample Index")
plt.ylabel("Global Active Power")
plt.tight_layout()
plt.show()