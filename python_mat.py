# # five graphs we will learn in this sessionn whole
# # types of data 
# # numerical data age,number,dob
# # categorical data,sumsung , apple university, gender

# # univariant analysis 
# # bivariant analysis
# # multivariant analysis


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt 
# import seaborn as sns

# df=pd.read_csv('sharma-kohli.csv')
# print(df.to_string())

# plt.plot(df['index'],df['V Kohli'],color="blue",
#          linestyle="solid",linewidth="2",marker=".",label='V Kohli')
# plt.plot(df['index'],df['RG Sharma'],color="black",
#          linestyle="dotted",linewidth="3",marker="o",label='RG Sharma')
# plt.title('Rohit and Virat Ipl Score Comparison Graph ')
# plt.xlabel("Year")
# plt.ylabel("Ipl Score")
# # plt.ylim(1,1000)
# # plt.xlim(2010,2020)
# plt.grid()
# plt.legend(loc='best')
# plt.show()

# scatter plot 
# bivariant 
# numerical and numerical
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('batter.csv')
df=df.head(50)
plt.scatter(df['avg'],df['strike_rate'])
plt.show()

# plt.plot(x,y,'o') works as a plt.scatter 
