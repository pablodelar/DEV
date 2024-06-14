import pandas as pd
import numpy as np

################################ From dict of Series or dicts ################################
d = {
   "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
   "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
   }

df = pd.DataFrame(d)
# print(df)

dfi = pd.DataFrame(d, index=["d", "b", "a"])
# print(dfi)

dfc = pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])
# print(dfc)

# print(dfc.index)
# print(dfc.columns)


################################ From dict of ndarrays or lists ################################
d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}

# x = pd.DataFrame(d)
x = pd.DataFrame(d, index=["a", "b", "c", "d"])
# print(x)


################################ From a list of dicts ################################
data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}] # A list of dicts

pd.DataFrame(data2)
pd.DataFrame(data2, index=["first", "second"])
pd.DataFrame(data2, columns=["a", "b"])