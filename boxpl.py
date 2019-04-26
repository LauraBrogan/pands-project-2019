#This will display to the user a box diagram of the dimentions of the sepal length for each of the three iris species.
#Import pandas program as pd.
import pandas as pd

#Import seaborn as sns
import seaborn as sns

#Import matpotlib.pyplot as plt.
import matplotlib.pyplot as plt

#This is setting the structure of the box plot. 
sns.set(style="whitegrid", palette="GnBu_d", rc={'figure.figsize':(11.7,8.27)})

#Iris_dats is reading in the data set csv file. 
iris_data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")

#Label the box chart with the title Comparing the Distributions of Sepal Length.
title="Comparing the Distributions of Sepal Length"

#Box plot x axis is the Species, y axis is the Sepal Length and the data is from irsi_data.
sns.boxplot(x="species", y="sepal_length", data=iris_data)

#Increasing font size of the title.
plt.title(title, fontsize=26)

#Show the plot
plt.show()

#Reference:https://seaborn.pydata.org/generated/seaborn.boxplot.html
#Laura Brogan 19/04/2019


