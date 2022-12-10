'''
Author: Samira Nassi
Group Members: Jade Born, Sergio Lopez
Date: 11/29/22
Class: ISTA 131
Section Leader: Olivia Fernflores
Description: Final Project
Horizontal bar chart of amount of homicides by ethnicity between 1980-2014
'''
import pandas as pd, numpy as np
import matplotlib.pyplot as plt;

# Using the database 'Homicide Reports 1980-2014' from Kaggle
columns = ['Record ID', 'State', 'City', 'Year', 'Crime Type', 'Weapon', 'Relationship',
           'Victim Sex', 'Victim Age', 'Victim Race', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race']
df = pd.read_csv('database.csv', usecols=columns, low_memory = False)

# Getting the amount of homicide reports of each ethnicity and sorting them by record id
victim_race = df.groupby(['Victim Race']).count().sort_values(by=['Record ID'])['Record ID']

# The subplot will take the index position on a grid with nrows rows and ncols columns
colors = ['salmon','indianred','tomato','lightcoral','orangered']
victim_race_chart, victim_race_ax = plt.subplots()

# Doing a horizonatal bar chart and setting up the axis
plt.figure(figsize=(8,4), tight_layout=True)
plt.barh(victim_race.index, victim_race.values, color = colors)
plt.title('Amount of Homicides by Ethnicity, 1980-2014',fontsize = 20)
plt.xlabel('Number of Homicides',fontsize = 18)
plt.ylabel('Ethnicity',fontsize = 18)
plt.show()