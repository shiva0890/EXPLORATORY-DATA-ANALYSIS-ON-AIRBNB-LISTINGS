# Import necessary libraries
import pandas as pd 
import matplotlib.pyplot as plt
# Load the Airbb dataset
df = pd.read_csv('AB_NYC_2019.csv')
# Display the first few rows of the dataset
print(df.head())
# Get basic statistics of the dataset
print(df.describe())
# Check for missing valuez
print(df.isnull().sum())

plt.hist(df['price'], bins=30, edgecolor='k')
plt.xlabel ('Number of Listings per Host')
plt.ylabel('Frequency')
plt.title ('Host Listing Distribution')
plt.show()

plt.hist(df['calculated_host_listings_count'], bins=2000, edgecolor='k')
plt.xlabel('Price (in $)')
plt.ylabel('Frequency')
plt.title('Price Distribution')
plt.show()

neighborhood_counts = df['neighbourhood_group'].value_counts()
neighborhood_counts.plot(kind='bar')
plt.xlabel('Neighborhood Group')
plt.ylabel('Count')
plt.title('Popular Neighborhood Groups')
plt.show()


room_type_counts = df ['room_type'].value_counts()
room_type_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Room Type Distribution')
plt.axis ('equal')
plt.show()