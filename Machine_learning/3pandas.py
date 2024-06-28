import pandas as pd
df=pd.read_csv('dirtydata.csv')
df.loc[7,'Duration']=30
print(df.to_string())
df.drop(7,inplace=True)
print(df.to_string())
for i in df.index:
    if df.loc[i,'Duration']>30:
        df.loc[i,'Duration']=300
        
print('\n')
print(df.head(9))
import pandas as pd
df=pd.read_csv('dirtydata.csv')
df.loc[7,'Duration']=30
print('\n')
print(df.to_string())
print(df.to_string())
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.to_string())