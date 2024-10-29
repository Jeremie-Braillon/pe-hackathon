# # Projet Hackathon - Christelle, Maxime, Jérémie, Pierre-Louis
#
# * Projet choisi _Le bonheur_
# * Objectif : définition d'un nouvelle indice de bonheur

# ## Importation des librairies

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import common as c
import seaborn as sns

# +
df = pd.read_csv('bonheur.csv', sep=';')

df['Healthy life expectancy at birth'] = pd.to_numeric(df['Healthy life expectancy at birth'], errors = 'coerce')
df['Healthy life expectancy at birth'].describe()

# +
df['GDP Normalisé'] = df['Log GDP per capita']/(df.loc[df['Log GDP per capita'].argmax(), 'Log GDP per capita'])
df['Esperance vie Normalisée'] = df['Healthy life expectancy at birth']/(df.loc[df['Healthy life expectancy at birth'].argmax(), 'Healthy life expectancy at birth'])


# Définition indice bonheur Maxime

df['Bonheur Maxime'] = df['Esperance vie Normalisée']
df.head(3)

# -

import seaborn as sns

df = pd.read_csv('bonheur.csv', sep=';')
df.head(2)

df['GDP Normalisé'] = df['Log GDP per capita']/(df.loc[df['Log GDP per capita'].argmax(), 'Log GDP per capita'])
df.head(3)



display(df.columns)




df['christelle']=df['Social support']+df['Generosity']
df['Generosity'].describe

df['Healthy life expectancy at birth']=pd.to_numeric(df['Healthy life expectancy at birth'],errors='coerce')
df.head(2)

# +


df['christelle']=df['Social support']+df['Generosity']+df['Healthy life expectancy at birth']*0.05+df['Freedom to make life choices']-df['Perceptions of corruption']
df.head(5)
# -


country=df.groupby(by='Country name')
country.size()

ind=df['christelle'].idxmax()
df.loc[ind]


# +
maxi=df['christelle'].max()
mini=df['christelle'].min()
print(maxi,mini)


display(df.head(4))
# -


