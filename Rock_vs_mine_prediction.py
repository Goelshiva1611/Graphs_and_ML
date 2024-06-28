import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

df=pd.read_csv('rock_mine.csv',header=None)
print(df.head())
print(df.describe())
print(df.groupby(60).mean())
print(df[60].value_counts())
X=df.iloc[:,0:60].values
y=df.iloc[:,-1].values

print(X.shape)
print(y.shape)

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.1,stratify=y,random_state=1)

clf=LogisticRegression()
clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)
y_train_test=clf.predict(x_train)

test=accuracy_score(y_pred,y_test)
train=accuracy_score(y_train,y_train_test)
print("Classification Report")
print("\n")
print( classification_report(y_test,y_pred))
print("\n")
print(confusion_matrix(y_test,y_pred))
print(f"Accuracy score for test data : {test}")
print(f"Accuracy score for train data : {train}")

print(clf.predict([[0.0286,0.0453,0.0277,0.0174,0.0384,0.0990,0.1201,0.1833,0.2105,0.3039,0.2988,0.4250,0.6343,0.8198,1.0000,0.9988,0.9508,0.9025,0.7234,0.5122,0.2074,0.3985,0.5890,0.2872,0.2043,0.5782,0.5389,0.3750,0.3411,0.5067,0.5580,0.4778,0.3299,0.2198,0.1407,0.2856,0.3807,0.4158,0.4054,0.3296,0.2707,0.2650,0.0723,0.1238,0.1192,0.1089,0.0623,0.0494,0.0264,0.0081,0.0104,0.0045,0.0014,0.0038,0.0013,0.0089,0.0057,0.0027,0.0051,0.0062]]))
print(clf.predict([[0.0352,0.0116,0.0191,0.0469,0.0737,0.1185,0.1683,0.1541,0.1466,0.2912,0.2328,0.2237,0.2470,0.1560,0.3491,0.3308,0.2299,0.2203,0.2493,0.4128,0.3158,0.6191,0.5854,0.3395,0.2561,0.5599,0.8145,0.6941,0.6985,0.8660,0.5930,0.3664,0.6750,0.8697,0.7837,0.7552,0.5789,0.4713,0.1252,0.6087,0.7322,0.5977,0.3431,0.1803,0.2378,0.3424,0.2303,0.0689,0.0216,0.0469,0.0426,0.0346,0.0158,0.0154,0.0109,0.0048,0.0095,0.0015,0.0073,0.0067]]))
print(clf.predict([[0.0179,0.0136,0.0408,0.0633,0.0596,0.0808,0.2090,0.3465,0.5276,0.5965,0.6254,0.4507,0.3693,0.2864,0.1635,0.0422,0.1785,0.4394,0.6950,0.8097,0.8550,0.8717,0.8601,0.9201,0.8729,0.8084,0.8694,0.8411,0.5793,0.3754,0.3485,0.4639,0.6495,0.6901,0.5666,0.5188,0.5060,0.3885,0.3762,0.3738,0.2605,0.1591,0.1875,0.2267,0.1577,0.1211,0.0883,0.0850,0.0355,0.0219,0.0086,0.0123,0.0060,0.0187,0.0111,0.0126,0.0081,0.0155,0.0160,0.0085]]))
print(clf.predict([[0.0180,0.0444,0.0476,0.0698,0.1615,0.0887,0.0596,0.1071,0.3175,0.2918,0.3273,0.3035,0.3033,0.2587,0.1682,0.1308,0.2803,0.4519,0.6641,0.7683,0.6960,0.4393,0.2432,0.2886,0.4974,0.8172,1.0000,0.9238,0.8519,0.7722,0.5772,0.5190,0.6824,0.6220,0.5054,0.3578,0.3809,0.3813,0.3359,0.2771,0.3648,0.3834,0.3453,0.2096,0.1031,0.0798,0.0701,0.0526,0.0241,0.0117,0.0122,0.0122,0.0114,0.0098,0.0027,0.0025,0.0026,0.0050,0.0073,0.0022]]))
print(clf.predict([[0.0329,0.0216,0.0386,0.0627,0.1158,0.1482,0.2054,0.1605,0.2532,0.2672,0.3056,0.3161,0.2314,0.2067,0.1804,0.2808,0.4423,0.5947,0.6601,0.5844,0.4539,0.4789,0.5646,0.5281,0.7115,1.0000,0.9564,0.6090,0.5112,0.4000,0.0482,0.1852,0.2186,0.1436,0.1757,0.1428,0.1644,0.3089,0.3648,0.4441,0.3859,0.2813,0.1238,0.0953,0.1201,0.0825,0.0618,0.0141,0.0108,0.0124,0.0104,0.0095,0.0151,0.0059,0.0015,0.0053,0.0016,0.0042,0.0053,0.0074]]))
print(clf.predict([[0.0191,0.0173,0.0291,0.0301,0.0463,0.0690,0.0576,0.1103,0.2423,0.3134,0.4786,0.5239,0.4393,0.3440,0.2869,0.3889,0.4420,0.3892,0.4088,0.5006,0.7271,0.9385,1.0000,0.9831,0.9932,0.9161,0.8237,0.6957,0.4536,0.3281,0.2522,0.3964,0.4154,0.3308,0.1445,0.1923,0.3208,0.3367,0.5683,0.5505,0.3231,0.0448,0.3131,0.3387,0.4130,0.3639,0.2069,0.0859,0.0600,0.0267,0.0125,0.0040,0.0136,0.0137,0.0172,0.0132,0.0110,0.0122,0.0114,0.0068]]))
