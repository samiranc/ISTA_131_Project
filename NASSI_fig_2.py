'''
Author: Samira Nassi
Group Members: Jade Born, Sergio Lopez
Date: 11/29/22
Class: ISTA 131
Section Leader: Olivia Fernflores
Description: Final Project
Scatterplot of Victim Count vs. Perpetrator Count
'''
import pandas as pd, numpy as np
import matplotlib.pyplot as plt;

# Using the database 'Homicide Reports 1980-2014' from Kaggle
columns = ['Record ID', 'State', 'City', 'Year', 'Crime Type', 'Weapon', 'Relationship',
           'Victim Sex', 'Victim Age', 'Victim Race', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Month','Victim Count', 'Perpetrator Count']
df = pd.read_csv('database.csv', usecols=columns, low_memory = False)

# Setting up the axis
x = df['Perpetrator Count'].mean()
y = df['Victim Count']

# Using plt.scatter function to build the scatterplot
plt.scatter(x=x,y=y)
plt.ylabel('Victim Count',fontsize = 20) #set the label for y axis
plt.xlabel('Perpetrator Count',fontsize = 18)
plt.title('Victim Count vs. Perpetrator Count',fontsize = 18)

# Equation for trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Adding trendline to plot
plt.plot(x, p(x), color ="purple", linewidth = 2, linestyle = "--")

# Showing the plot!!!
plt.show()
