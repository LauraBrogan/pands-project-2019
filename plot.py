
import pandas as pd
import matplotlib.pyplot as plt




df = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")

x = df.species
y = df.sepal_length
plt.scatter(x, y)
plt.show()



# Reference:https://ourcodingclub.github.io/2018/04/18/pandas-python-intro.html#following