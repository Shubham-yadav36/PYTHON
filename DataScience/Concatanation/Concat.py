import pandas as pd
list1 = ['ram','lakhan','shyam']
list2 = ['cricket','golf','player']
df = pd.DataFrame({'Name':list1,'Game':list2})
# print(df)

list3 = ['shyam','karan','ramu']
list4 = ['badminton','khokho','kabbaddi']
df1 = pd.DataFrame({'Name':list1,'Game':list2})
# print(df1)

print(pd.concat([df,df1]))