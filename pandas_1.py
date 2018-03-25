
import pandas as pd
df=pd.read_csv("PastHires.csv")
#df[['Previous employers','Hired']]
df.head()#first 5 rows
df[['Previous employers','Hired']][5:11].plot(kind='bar')
