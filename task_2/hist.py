import pandas as pd

#Importer le dataset

df=pd.read_csv('housing.csv')

#Voir la distribution pour la variable bedrooms avec matplotlib
import matplotlib.pyplot as plt
plt.hist(df['bedrooms'],bins=10,edgecolor='black')
plt.title('Distribution de la variable bedrooms')
plt.xlabel('Bedrooms')
plt.show()