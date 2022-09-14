import pandas
import numpy as np
import plotly.express as px

iris_df = pandas.read_csv("iris.data", header=None)
iris_df.columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]

iris_np = iris_df.drop('class', axis=1)
iris_np1 = np.array(iris_np)
mean = np.mean(iris_np1, axis=0)
Max = np.max(iris_np1, axis=0)
Min = np.min(iris_np1, axis=0)
print(mean)
print(Max)
print(Min)

fig1 = px.scatter(iris_df, x="sepal length", y="sepal width")
fig1.show()

df = px.data.tips()
fig2 = px.histogram(iris_df, x="class", color="sepal length")
fig2.show()

df = px.data.tips()
fig3 = px.violin(iris_df, y="petal length", x="petal width", color="class", box=True, points="all", hover_data=iris_df.columns)
fig3.show()










