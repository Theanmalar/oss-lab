from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

print(&quot;X_train:&quot;, X_train)
print(&quot;X_test:&quot;, X_test)
print(&quot;y_train:&quot;, y_train)
print(&quot;y_test:&quot;, y_test)

