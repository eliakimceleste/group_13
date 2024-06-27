import pandas as pd
import matplotlib.pyplot as plt
#Importer le dataset

df=pd.read_csv('./Housing.csv')

#Voir la distribution pour la variable bedrooms avec matplotlib
plt.hist(df['bedrooms'],bins=10,edgecolor='black')
plt.title('Distribution de la variable bedrooms')
plt.xlabel('Bedrooms')
plt.show()