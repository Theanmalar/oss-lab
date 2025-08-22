from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

data = {
    'Maths': [30, 60, 55, 70, 90, 30, 45, 80],
    'Science': [35, 90, 60, 75, 85, 60, 30, 90],
    'Passed': [0, 0, 1, 1, 1, 0, 0, 1]
}
df = pd.DataFrame(data)
X = df[['Maths', 'Science']]
y = df['Passed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.50, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Predictions:", y_pred.tolist())
print("Actual:", y_test.tolist())


import pandas as pd
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
'Maths': [30, 45, 55, 70, 90, 20, 35, 80],
'Science': [35, 40, 60, 75, 85, 25, 30, 90],
'Total': [65, 85, 115, 145, 175, 45, 65, 170] 
}

df = pd.DataFrame(data)

X = df[['Maths', 'Science']]
y = df['Total'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print( "Score:", r2_score(y_test, y_pred))
print("Predictions:", y_pred.tolist())
print("Actual: ", y_test.tolist())

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
data = {
'Maths': [30, 45, 55, 70, 90, 20, 35, 80],
'Science': [35, 40, 60, 75, 85, 25, 30, 90],
'Passed': [0, 0, 1, 1, 1, 0, 0, 1] # Target variable (label)
}
df = pd.DataFrame(data)
X = df[['Maths', 'Science']]
y = df['Passed']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
print("Predictions:", y_pred.tolist())
print("Actual:", y_test.tolist())

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
data = {
'Maths': [30, 45, 55, 70, 90, 20, 35, 80],
'Science': [35, 40, 60, 75, 85, 25, 30, 90],
'Passed': [0, 0, 1, 1, 1, 0, 0, 1] # Target variable (label)
}
df = pd.DataFrame(data)
X = df[['Maths','Science']]
y = df['Passed']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Predictions:", y_pred.tolist())
print("Actual: ", y_test.tolist())

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
data = {
&#39;Maths&#39;: [30, 45, 55, 70, 90, 20, 35, 80],
&#39;Science&#39;: [35, 40, 60, 75, 85, 25, 30, 90],
&#39;Passed&#39;: [0, 0, 1, 1, 1, 0, 0, 1] # Target variable (label)
}
df = pd.DataFrame(data)
X = df[[&#39;Maths&#39;, &#39;Science&#39;]]
y = df[&#39;Passed&#39;]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = KNeighborsClassifier(n_neighbors=3) # You can adjust the number of neighbors
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(&quot;Accuracy:&quot;, accuracy_score(y_test, y_pred))
print(&quot;\nClassification Report:\n&quot;, classification_report(y_test, y_pred))
print(&quot;Predictions:&quot;, y_pred.tolist())
print(&quot;Actual:&quot;, y_test.tolist())

import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
data = {
&#39;Maths&#39;: [30, 45, 55, 70, 90, 20, 35, 80],
&#39;Science&#39;: [35, 40, 60, 75, 85, 25, 30, 90],
&#39;Passed&#39;: [0, 0, 1, 1, 1, 0, 0, 1] # Target variable (label)
}
df = pd.DataFrame(data)
X = df[[&#39;Maths&#39;, &#39;Science&#39;]]
y = df[&#39;Passed&#39;]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = SVC(kernel=&#39;linear&#39;, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(&quot;Accuracy:&quot;, accuracy_score(y_test, y_pred))
print(&quot;\nClassification Report:\n&quot;, classification_report(y_test, y_pred))
print(&quot;Predictions:&quot;, y_pred.tolist())
print(&quot;Actual:&quot;, y_test.tolist())

