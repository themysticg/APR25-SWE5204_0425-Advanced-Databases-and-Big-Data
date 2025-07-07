# 📌 Task 3: Video Game Sales Analysis

# ▶️ Data Acquisition
import pandas as pd

# Load dataset (update path if you save it locally)
df = pd.read_csv('vgsales.csv')

# Preview data
df.head()

# ▶️ Data Wrangling
# Check missing values
df.isnull().sum()

# Drop rows with missing critical info (Name, Year, Genre, Global_Sales)
df_clean = df.dropna(subset=['Name', 'Year', 'Genre', 'Global_Sales'])

# Confirm cleaning
df_clean.info()

# ▶️ Descriptive Analysis
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of Global Sales
plt.figure(figsize=(8,5))
sns.histplot(df_clean['Global_Sales'], bins=50, kde=True)
plt.title('Distribution of Global Sales')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Frequency')
plt.show()

# Top 10 Genres by Global Sales
top_genres = df_clean.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title('Top 10 Genres by Global Sales')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Genre')
plt.show()

# ▶️ Scatter Plot: Critic Score vs Global Sales
# Filter rows with Critic_Score available
if 'Critic_Score' in df_clean.columns:
    df_scores = df_clean.dropna(subset=['Critic_Score'])
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df_scores, x='Critic_Score', y='Global_Sales')
    plt.title('Critic Score vs Global Sales')
    plt.xlabel('Critic Score')
    plt.ylabel('Global Sales (millions)')
    plt.show()
else:
    print("Column 'Critic_Score' not found in dataset.")

# ▶️ Diagnostic Analysis: Regression
from sklearn.linear_model import LinearRegression
import numpy as np

if 'Critic_Score' in df_clean.columns:
    X = df_scores['Critic_Score'].values.reshape(-1,1)
    y = df_scores['Global_Sales'].values.reshape(-1,1)

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Plot regression line
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=X.flatten(), y=y.flatten(), label='Data')
    plt.plot(X, y_pred, color='red', label='Regression Line')
    plt.title('Regression: Critic Score vs Global Sales')
    plt.xlabel('Critic Score')
    plt.ylabel('Global Sales (millions)')
    plt.legend()
    plt.show()

    # Correlation heatmap
    corr = df_scores[['Critic_Score', 'Global_Sales']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
else:
    print("Skipping regression: 'Critic_Score' not found in dataset.")

# ▶️ Conclusions
# In Markdown cell, summarize findings:
# - Which genres perform best
# - Whether critic scores correlate with sales
# - Recommendations for game developers/publishers
