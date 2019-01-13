import pandas as pd 
import numpy as np
# date time
# df1 = pd.date_range("20180101", "20180110")
# df2 = pd.date_range("20170101", "20170110")
# minh = range(10)
# minh = {"A": df1, "B": df2, "C" : minh}
# a = pd.DataFrame(minh)

# plot Dataframe in int
df = pd.DataFrame(np.random.randn(10,2), columns = ['a', 'b'])
print(df.plot.bar())