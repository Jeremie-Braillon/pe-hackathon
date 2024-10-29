# # Projet Hackathon - Christelle, Maxime, Jérémie, Pierre-Louis
#
# * Projet choisi _Le bonheur_
# * Objectif : définition d'un nouvelle indice de bonheur

# ## Importation des librairies

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import common as c

df = pd.read_csv('bonheur.csv', sep=';')
df.head(2)

df['GDP Normalisé'] = df['Log GDP per capita']/(df.loc[df['Log GDP per capita'].argmax(), 'Log GDP per capita'])
df.head(3)
