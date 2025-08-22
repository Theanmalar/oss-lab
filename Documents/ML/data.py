import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.rand(5,3),index=['a','h','c','g','e'],columns=['one','two','three'])
print("column 'two' with non null values:")
print(df['two'].dropna())
print("\ncolumn 'one' with nans filled with 100:")
print(df['one'].fillna(100))
print("\ncolumn 'one' with rows containing nans dropped:")
print(df['one'].dropna())
  df2=pd.DataFrame({'one':[10,20,30,40,50,2000],'two':[1000,0,30,50,60,40]})
print("\nDataFrame with values replaced:")
print(df2.replace({1000: np.nan, 10: 1,2000: 2,20:3}))

import pandas as pd
import numpy as np
 df = pd.DataFrame(np.random.rand(5,3),index=['a','h','c','i','e'],columns=['one','two','three'])
 df = df.reindex(['a','b','c','d','e','f','g','h'])
print(df)
print(df.isnull())
print(df.notnull())

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), index=['a', 'h', 'c', 'i', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print(df.isnull())
print(df.notnull())




