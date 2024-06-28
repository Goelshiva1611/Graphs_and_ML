import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
df=pd.read_csv('play_tennis.csv')
df.drop(columns='day',inplace=True)
print(df.head())
print(df['play'].value_counts())
py=9/14
pn=5/14

print(pd.crosstab(df['outlook'],df['play']))
print('\n')
print(pd.crosstab(df['temp'],df['play']))
print('\n')
print(pd.crosstab(df['humidity'],df['play']))
print('\n')
print(pd.crosstab(df['wind'],df['play']))
print('\n')

pon=0
poy=4/9
prn=2/5
pry=3/9
psn=3/5
psy=2/9

pcooln=1/5
pcooly=3/9
photn=2/5
photy=2/9
pmildn=2/5
pmildy=4/9

phumidn=0
phumidy=0
phighn=4/5
phighy=3/9
pnormaln=1/5
pnormaly=6/9

pwindn=0
pwindy=0
pstringn=3/5
pstringy=3/9
pweakn=2/5
pweaky=6/9

pyes=py*psy*photy*phighy*pweaky
print(pyes)
pno=pn*psn*photn*phighn*pweakn
print(pno)
if(pyes>pno):
    print('Yes,You Can Play Tennis')
else:
    print('NO,You Can not Play Tennis')



