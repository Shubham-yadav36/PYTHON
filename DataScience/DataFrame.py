# creating the list using list
import pandas as pd
data = [5,4,7,8,5]
sc = pd.DataFrame(data)
print(sc)

fruit = {'fruit' :['apple','banana'],'name':['Ram','Shyam']}
df = pd.DataFrame(fruit)
print(df)