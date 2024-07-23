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
#dropping row
xfdf=pd.DataFrame(data)
print(xfdf)
xfdf=xfdf.drop([1,2])
print(xfdf)
#dropping column
xsds=pd.DataFrame(data)
xsds=xsds.drop(['Name'],axis=1)
xsds=xsds.drop([3],axis=0)
print(xsds)
#filtering
xsdf=pd.DataFrame(data)
xsdf=xxdf.filter(['R.No','Name','Percentage','%'])
print(xsdf)
xssf=xxdf.filter(like='Pe')
print(xssf)
#sorting
sdf=xxdf.sort_values('marks',ascending=False)
print(sdf)
