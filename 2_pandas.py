import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())
print('\n')
print(pd.options.display.max_rows)
print('\n')
print(df)

import pandas as pd
shiva={
    "hello":
        {
            "Key": 1,
            "value":2,
            "system":3,            
            "Key2": 1,
            "value3":2,
            "system3":3
        },
    "hyee":
        {
            "Key": 1,
            "value":2,
            "system":3,
            "Key1": 1,
            "value1":2,
            "system1":3
        },
    "hiiiii":
        {
            "Key": 1,
            "value":2,
            "system":3
        },
    "huuuyyyyr":
        {
            "Key": 1,
            "value":2,
            "system":3
        }    
}

newshiva={
    "matlab":[1,2,3,4,5],
    "seaborn":[1,2,3,4,5],
    "matplotlib":[1,2,3,4,5],
    "numpy":[1,2,3,4,5]
}
newshiva1=pd.DataFrame(newshiva,index=["x","y","z","u","v"])
print(newshiva1)
print("\n")

shivanew=pd.DataFrame(shiva)
print(shivanew)

# here is the easy way to view the day easily 
import pandas as pd
shiva=pd.read_csv('data.csv')
print(shiva.head())
print(shiva.tail())

# what you want the info about the dataframe

print(shiva.info())

# cleaning of data in the pandas 
# puri row ko hatao
import pandas as pd
df=pd.read_csv('data.csv')
print(df.head())
# empty cell it will give you wrong result always
# puri row ko hatao
dfnew =df.dropna()

# if you want to make change in the original datagrame 
df.dropna(inplace=True)
df.dropna(subset="date",inplace=True)
#  inorder to fill the empty cell what you can do
df["calories"].fillna(13,inplace=True)
