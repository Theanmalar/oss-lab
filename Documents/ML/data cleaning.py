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


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), index=['a', 'h', 'c', 'g', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print(df['one'].isnull())
print(df['one'].bfill())
print (df['one'].notnull())
print(['one'].fillna(10))
print(['one'].dropna())
print(['one'].pad())

import numpy as np
from sklearn.decomposition
import PCA
import matplotlib.pyplot as plt

data = np.array([[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9]
                ])

pca = PCA(n_components=1)


transformed_data = pca.fit_transform(data)

plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1])
plt.title(Original Data (2 Features))
plt.xlabel(Feature A)
plt.ylabel(Feature B)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(transformed_data, np.zeros_like(transformed_data)) 
plt.title(&#39;Transformed Data (1 Principal Component)&#39;)
plt.xlabel(&#39;Principal Component 1&#39;)
plt.yticks([]) 
plt.grid(True)

plt.tight_layout()
plt.show()

print(&quot;Original Data Shape:&quot;, data.shape)
print(&quot;Transformed Data Shape:&quot;, transformed_data.shape)

print(&quot;Transformed Data (First 5 rows):\n&quot;, transformed_data[:5])

import numpy as np
from sklearn.decomposition
import PCA
import matplotlib.pyplot as plt

data = np.array([[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9]
                ])

pca = PCA(n_components=1)


transformed_data = pca.fit_transform(data)

plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1])
plt.title(Original Data (2 Features))
plt.xlabel(Feature A)
plt.ylabel(Feature B)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(transformed_data, np.zeros_like(transformed_data)) 
plt.title(&#39;Transformed Data (1 Principal Component)&#39;)
plt.xlabel(&#39;Principal Component 1&#39;)
plt.yticks([]) 
plt.grid(True)

plt.tight_layout()
plt.show()

print(&quot;Original Data Shape:&quot;, data.shape)
print(&quot;Transformed Data Shape:&quot;, transformed_data.shape)

print(&quot;Transformed Data (First 5 rows):\n&quot;, transformed_data[:5])

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Sample data
data = np.array([
    [1, 2], [2, 3], [3, 4], [4, 5],
    [5, 6], [6, 7], [7, 8], [8, 9]
])

# Apply PCA to reduce to 1 component
pca = PCA(n_components=1)
transformed_data = pca.fit_transform(data)

# Plot original data
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1])
plt.title('Original Data (2 Features)')
plt.xlabel('Feature A')
plt.ylabel('Feature B')
plt.grid(True)

# Plot transformed data
plt.subplot(1, 2, 2)
plt.scatter(transformed_data, np.zeros_like(transformed_data))
plt.title('Transformed Data (1 Principal Component)')
plt.xlabel('Principal Component 1')
plt.yticks([])
plt.grid(True)

plt.tight_layout()
plt.show()

print("Original Data Shape:", data.shape)
print("Transformed Data Shape:", transformed_data.shape)
print("Transformed Data (First 5 rows):\n", transformed_data[:5])



import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


data = np.array([
    [1, 2], [2, 3], [3, 4], [4, 5],
    [5, 6], [6, 7], [7, 8], [8, 9]
])


pca = PCA(n_components=1)
transformed_data = pca.fit_transform(data)


plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1])
plt.title('Original Data (2 Features)')
plt.xlabel('Feature A')
plt.ylabel('Feature B')
plt.grid(True)


plt.subplot(1, 2, 2)
plt.scatter(transformed_data, np.zeros_like(transformed_data))
plt.title('Transformed Data (1 Principal Component)')
plt.xlabel('Principal Component 1')
plt.yticks([])
plt.grid(True)

plt.tight_layout()
plt.show()

print("Original Data Shape:", data.shape)
print("Transformed Data Shape:", transformed_data.shape)
print("Transformed Data (First 5 rows):\n", transformed_data[:5])



