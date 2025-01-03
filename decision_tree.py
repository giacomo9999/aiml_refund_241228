import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("decision-tree-test-data.csv")

d = {"UK": 0, "USA": 1, "N": 2}
df["Nationality"] = df["Nationality"].map(d)
d = {"YES": 1, "NO": 0}
df["Go"] = df["Go"].map(d)

features = ["Age", "Experience", "Rank", "Nationality"]

X = df[features]
y = df["Go"]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X.values, y.values)

tree.plot_tree(dtree, feature_names=features)
plt.show()

print(dtree.predict([[40, 10, 7, 1]]))
