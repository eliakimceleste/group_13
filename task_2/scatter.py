import pandas as pd
import matplotlib.pyplot as plt
#Importer le dataset

df=pd.read_csv('task_2/Housing.csv')

#Faire le nuage de point avec la variable price en ordonnées et la variable area en abscisse

plt.scatter(df['area'],df['price'],alpha=1)
plt.title('Nuage de point de la superficie et du prix')
plt.xlabel('Area')
plt.ylabel('Price')  
plt.show()
