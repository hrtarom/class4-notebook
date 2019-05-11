
import numpy as np
import pandas as pd
import argparse

data= pd.read_csv('breast_cancer.csv')
Data=pd.DataFrame(data)
for col  in range(len(Data.columns)):
    print ("The mean of the",Data.columns[col],"is",Data.iloc[:,col].mean())
    print ("The standard deviation of the",Data.columns[col],"is",Data.iloc[:,col].std())
    print ("\n")



