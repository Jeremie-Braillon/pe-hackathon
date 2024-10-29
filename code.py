# # Projet Hackathon - Christelle, Maxime, Jérémie, Pierre-Louis
#
# * Projet choisi _Le bonheur_
# * Objectif : définition d'un nouvelle indice de bonheur

# ## Importation des librairies

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import common as c

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


