import pandas as pd
import csv 

df = pd.read_csv("final.csv")

df['Distance'] = df['Distance'].apply(lambda x: x.replace(',', ''))

for i , d in enumerate(df['Distance']):
    if float(d) <= 100:
        print(i)
        print("ok")
    else:
        print(i)
        print("not ok")
        df.drop(index = i,inplace = True)

print("================================================================================================================")

for i , d in enumerate(df['Gravity']):
    if float(d) >= 150 or float(d) <= 350:
        print(i)
        print("ok")
    else:
        print(i)
        print("not ok")
        df.drop(index = i,inplace = True)

df.to_csv("new.csv")
