import pandas as pd
df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
print(df)
nr={'A':7,'B':8}
df=df._append(nr,ignore_index=True)
print(df)
#or
import pandas as pd
xdf1=pd.DataFrame({'Name':['John','Jane'],'Age':[25,20]})
xdf2=pd.DataFrame({'Name':['Peter','Paul'],'Age':[35,30]})
xdf3=pd.DataFrame({'Name':['Tony','Pepper'],'Age':[25,20]})
xdf=pd.concat([xdf1,xdf2,xdf3],ignore_index=True)
print(xdf)
