import pandas as pd
series = [1,2,5,10,25,50]
sr =pd.Series(series)
print(sr)
print(type(sr))
# changing the index type 
series1 = [1,2,5,4]
sr = pd.Series(series1,index = ['a','b','c','d'])
print(sr)
s