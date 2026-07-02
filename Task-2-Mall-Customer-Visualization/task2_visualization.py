import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Histogram - Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"])
plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.show()

# Bar Chart
genre_count = df["Genre"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(genre_count.index, genre_count.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()