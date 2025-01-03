import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("csmith_data_2.csv")
# df = pandas.read_csv("order-data.csv")


features = ["Amount", "Years", "PriorRequests", "AcctsOnIP"]

X = df[features]
y = df["Outcome"]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X.values, y.values)

plt.figure(figsize=(20, 10))
tree.plot_tree(dtree, feature_names=features, filled=True)

plt.show()

print(dtree.predict([[25, 3, 0, 1]]))
print(dtree.predict([[1154, 0.1, 10, 15]]))
