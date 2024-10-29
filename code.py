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

#On corrige les colonnes à la con
df['Healthy life expectancy at birth'] = pd.to_numeric(df['Healthy life expectancy at birth'], errors = 'coerce')

# +
#On normalise le GDP et l'espérance de vie

df['GDP Normalisé'] = df['Log GDP per capita']/(df.loc[df['Log GDP per capita'].argmax(), 'Log GDP per capita'])
df['Esperance vie Normalisée'] = df['Healthy life expectancy at birth']/(df.loc[df['Healthy life expectancy at birth'].argmax(), 'Healthy life expectancy at birth'])

df.head(5)

# +
#Garder que la dernière année pour chaque pays
# -

#Indice du bonheur, sans tenir compte du PIB
df['Indice bonheur'] = (df['Social support'] + df['Freedom to make life choices']*4 + df['Generosity']*0.7 + (1-df['Perceptions of corruption'])*5 + df['Positive affect'] + df['Esperance vie Normalisée'])/15.7
# Score de développement du pays
df['Score développement'] = (df['Freedom to make life choices'] + (1-df['Perceptions of corruption'])*10 + df['GDP Normalisé']*7 + df['Esperance vie Normalisée']*10)/28


# +
#Création colonne heureux / pas heureux + donner pays le plus / moins heureux

# +
#Tracés de corrélation :

display(df.plot.scatter(x='GDP Normalisé', y='Indice bonheur'))
# On constate que le PIB ait une influence, il faut que le PIB soit très élevé. Sinon, les gens s'en moquent
display(df.plot.scatter(x='Generosity', y='Indice bonheur'))
# Aucune influence notable

display(df.plot.scatter(x='Generosity', y='GDP Normalisé'))
# Constat intéressant : plus le PIB/hab est élevé, moins les gens sont généreux !!

display(df.plot.scatter(x='Score développement', y='Generosity'));
# Aucune influence notable
display(df.plot.scatter(x='Score développement', y='Indice bonheur'));
# Globalement, les gens sembent être d'autant plus heureux que le pays est développé !
# -

# Filter the DataFrame for France
df_france = df[df['Country name'] == 'France']

# Plot the evolution of 'Indice de bonheur' through time
plt.figure(figsize=(10, 6))
plt.plot(df_france['year'], df_france['Indice bonheur'], marker='o')
plt.title("Evolution de l'Indice de bonheur en France")
plt.xlabel('Année')
plt.ylabel('Indice de bonheur')
plt.grid(True)
plt.show()


# Garder uniquement la dernière année pour chaque pays
df_last_year = df.loc[df.groupby('Country name')['year'].idxmax()]

# Trier les pays par 'Indice bonheur' décroissant et prendre les premiers
top_happy_countries = df_last_year.sort_values(by='Indice bonheur', ascending=False).head(30)

# Créer un barchart pour les premiers pays les plus heureux
plt.figure(figsize=(12, 8))
sns.barplot(x='Indice bonheur', y='Country name', data=top_happy_countries, palette='viridis')
plt.title('Pays les plus heureux')
plt.xlabel('Indice de bonheur')
plt.ylabel('Pays')
plt.show()

# Trier les pays par 'GDP Normalisé' décroissant et prendre les remiers
top_gdp_countries = df_last_year.sort_values(by='GDP Normalisé', ascending=False).head(30)

# Créer un barchart pour les 10 premiers pays avec le PIB le plus élevé
plt.figure(figsize=(12, 8))
sns.barplot(x='GDP Normalisé', y='Country name', data=top_gdp_countries, palette='viridis')
plt.title('Pays avec le PIB le plus élevé')
plt.xlabel('GDP Normalisé')
plt.ylabel('Pays')
plt.show()




