import pandas as pd
data={'R.No.':[1,2,3,4,5],'Name':['A','B','C','D','E'],'marks':[99,80,89,90,91]}
xxdf=pd.DataFrame(data)
print(xxdf)
xxdf['Percentage']=(xxdf['marks']/100)*100
xxdf['%']='%'
print(xxdf)
xdf=pd.DataFrame(data)
xdf=xdf.assign(Address=['Delhi','Noida','New Delhi',"Mumbai",'Banglore'])
print(xdf)
xfdf=pd.DataFrame(data)
print(xfdf)
xfdf=xfdf.drop([1,2])
print(xfdf)
