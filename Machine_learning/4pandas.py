# iloc is integer loaction function
#datframe.iloc[row_loc,column ]

# selecting a single elemnet 
# dataframe.iloc[row,coloum]

import pandas as pd
df={'Name':['Piyush','Shivansh','Manish','Lavish'],
    'Age':[20,30,40,50],
    'Country':['Dubai','Canada','Oman','Qatar']}
dfnew=pd.DataFrame(df,index=[1,2,3,4])
print(dfnew.to_string())

print('\n')

element=dfnew.iloc[1,2]
print(element)
print('\n')

subset=dfnew.iloc[0:3,0:2]
print(subset)
print('\n')
dfnew=pd.DataFrame(df,index=pd.MultiIndex.from_tuples([('D',1),('D',2),('Q',3),('Q',4)],names=['N','V']))
print(dfnew)

dfnew=pd.DataFrame([[4,5,6],[7,8,9],[10,11,12]],columns=["a","b","c"],index=[1,2,3])
print("\n")
print(dfnew)