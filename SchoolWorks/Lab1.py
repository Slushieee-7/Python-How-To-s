import pandas as pd

#for one-dimensional
mydataset = [2, 0, 2, 2]

#for one-dimensional
myvar = pd.Series(mydataset)

#creating label index
myvar = pd.Series(mydataset, index = ["a", "k", "i"])
