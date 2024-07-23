import pandas as pd
data={'R.No.':[1,2,3,4,5,'Name':['A','B','C','D','E'],'marks':[99,80,89,90,91]}
xdf=pd.DataFrame(data)
print(xdf)
xdf['Percentage']=((xdf['marks']/100)*100,'%')
print(xdf)
