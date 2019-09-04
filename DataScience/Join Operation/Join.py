import pandas as pd
player = ['shubham','amit','dharam']
course = ['MCA','MSC','CCTNS']
city = ['bhopal','datia','dewas']
data = pd.DataFrame({'Player':player,'Course':course,'City':city})

player = ['rj','amit','dharam']
course = ['MCA','MDD','CCNA']
city = ['bhopal','datia','indore']
data1 = pd.DataFrame({'Player':player,'Course':course,'City':city})
print(data1.join(data,how='outer'))