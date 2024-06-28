#  a pandas series is a column in a table . i ias just like a 2d array which holds any type of data 
import pandas as pd
shivansh=[1,7,2]
shivanshnew =pd.Series(shivansh)
print(shivanshnew)
# labelling will be done at there 
import pandas as pd1
shiv=[1,2,1]
shivanwew=pd.Series(shiv)
print(shivanwew[0])

# with create label and you can crete your name own labels 

shivanwew=pd.Series(shiv,index=["x","y","z"])
print(shivanwew["x"])

