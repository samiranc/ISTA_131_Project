'''
Author: Samira Nassi
Group Members: Jade Born, Sergio Lopez
Date: 11/29/22
Class: ISTA 131
Section Leader: Olivia Fernflores
Description: Final Project
Bar chart of victim's age on homicide reports between 1980 and 2014
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Using the database 'Homicide Reports 1980-2014' from Kaggle
columns = ['Record ID', 'State', 'City', 'Year', 'Crime Type', 'Weapon', 'Relationship',
           'Victim Sex', 'Victim Age', 'Victim Race', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Agency Name']
df = pd.read_csv('database.csv', usecols=columns, low_memory = False)

# Getting the amount of homicide reports of each victims age and sorting them by record id
victim_age = df.groupby(['Victim Age']).count().sort_values(by=['Record ID'])['Record ID']
victim_age_chart, victim_age_ax = plt.subplots()

# Bar chart and setting up axis titles
plt.bar(victim_age.index, victim_age.values)
plt.ylabel('Amount of Homicides', fontsize = 18) #set the label for y axis
plt.xlabel('Victim Age',fontsize = 18) #set the label for x-axis
plt.title('Victims Age on Homicide Reports, 1980-2014', fontsize = 20) #set the title of the graph
plt.legend()
plt.show() #display the graph