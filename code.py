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
#On ouvre le csv
df = pd.read_csv('bonheur.csv', sep=';')
display(df.head(5))

#On corrige les colonnes à la con
df['Healthy life expectancy at birth'] = pd.to_numeric(df['Healthy life expectancy at birth'], errors = 'coerce')

# +
#On normalise le GDP et l'espérance de vie

df['GDP Normalisé'] = df['Log GDP per capita']/(df.loc[df['Log GDP per capita'].argmax(), 'Log GDP per capita'])
df['Esperance vie Normalisée'] = df['Healthy life expectancy at birth']/(df.loc[df['Healthy life expectancy at birth'].argmax(), 'Healthy life expectancy at birth'])
df.head(5)
# -

#Garder que la dernière année pour chaque pays
df2 = df.drop_duplicates(subset = 'Country name', keep = 'last')
# -

#Indice du bonheur
df['Indice bonheur'] = (df['Social support'] + df['Freedom to make life choices'] + df['Generosity'] + df['Perceptions of corruption'] + df['Positive affect'] + df['GDP Normalisé'] + df['Esperance vie Normalisée'])/7
df.head(5)

# +
#Création colonne heureux / pas heureux + donner pays le plus / moins heureux
maxi=df["Indice bonheur"].max()
mini=df["Indice bonheur"].min()

int=(maxi-mini)/3
ind2=mini+int
ind3=mini+int*2
ind4=maxi+1

print(maxi,mini)
