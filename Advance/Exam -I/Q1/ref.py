import pandas as pd
import matplotlib.pyplot as plt

goi=pd.read_csv("GOI - GOI.csv")
goi

goistates = goi[['Country/ States/ Union Territories Name',
                'Literacy Rate (Persons) - Rural - 2001',
                'Literacy Rate (Persons) - Urban - 2001']]


plt.figure(figsize=(12, 8))
plt.scatter(goistates['Literacy Rate (Persons) - Rural - 2001'],
            goistates['Literacy Rate (Persons) - Urban - 2001'],
            color='red', alpha=0.6)


plt.title('Relationship between Rural and Urban Literacy Rates (2011)')
plt.xlabel('Literacy Rate (Rural)')
plt.ylabel('Literacy Rate (Urban)')


for i, states in enumerate(goistates['Country/ States/ Union Territories Name']):
    plt.annotate(states, (goistates.iloc[i]['Literacy Rate (Persons) - Rural - 2001'],
                         goistates.iloc[i]['Literacy Rate (Persons) - Urban - 2001']),
                 textcoords="offset points", xytext=(0, 4), ha='center')


plt.show()
