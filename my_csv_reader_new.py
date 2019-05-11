
import numpy as np
import pandas as pd
import argparse,sys

data= pd.read_csv(sys.argv[1])
Data=pd.DataFrame(data)
for col  in range(len(Data.columns)):
    print ("The mean of the",Data.columns[col],"is",Data.iloc[:,col].mean())
    print ("The standard deviation of the",Data.columns[col],"is",Data.iloc[:,col].std())
    print ("\n")



