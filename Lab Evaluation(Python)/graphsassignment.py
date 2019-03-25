import pandas as pd
#import seaborn as sns
mydata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mydata)
mydata.columns=["Col1","Col2","Col3","Col4","Col5"]
print(mydata.Col3)
mydata['Col6']=mydata["Col2"].map(str)+":"+mydata["Col3"]
print(mydata)
print(mydata.columns.tolist())
#mydata=pd.DataFrame({'Col4':[], 'Col1':[]})
mydata.plot.bar(x='Col4'[:10],y='Col1'[:10],rot=90)
#sns.barplot(x='Col4', y='Col1', data=mydata)


