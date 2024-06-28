import pandas as pd
df=pd.read_csv('dirtydata.csv')
# print(df.to_string())
# print("\n")
# dfnew=df.dropna()
# print(dfnew.to_string())

# df.dropna(inplace=True)
# print(df.to_string())
# df['Calories'].fillna(190,inplace=True)
print(df.to_string())
df["Date"]=pd.to_datetime(df['Date'],errors='coerce', infer_datetime_format=True)
print(df.to_string())