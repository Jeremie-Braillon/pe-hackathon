import pandas as pd
import numpy as np

df = pd.read_csv('bonheur.csv', sep=';')
df.head(2)

df['GDP Normalisé'] = df['Log GDP per capita']/(df.loc[df['Log GDP per capita'].argmax(), 'Log GDP per capita'])
df.head(3)


