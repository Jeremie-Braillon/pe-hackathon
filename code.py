# +
import pandas as pd
import numpy as np
import seaborn as sns

df=pd.read_csv('bonheur.csv',sep=';')
display(df.head(2))

display(df.columns)



# +
df['christelle']=df['Social support']+df['Generosity']
df['Generosity'].describe

df['Healthy life expectancy at birth']=pd.to_numeric(df['Healthy life expectancy at birth'],errors='coerce')

df['christelle']=df['Social support']+df['Generosity']+df['Healthy life expectancy at birth']*0.05+df['Freedom to make life choices']-df['Perceptions of corruption']
df.head(5)

# +
country=df.groupby(by='Country name')
country.size()

ind=df['christelle'].idxmax()
df.loc[ind]


# -

maxi=df['christelle'].max()
mini=df['christelle'].min()
print(maxi,mini)

nouvelle_col=pd.cut('christelle',bins=
