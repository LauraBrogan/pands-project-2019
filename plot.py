#This code is to display a scatter diagram of the petal lenght of the 3 varities of Iris flower. 
#I import pands as pd and matplotlib.pyplot as plt. 
import pandas as pd
import matplotlib.pyplot as plt

# I read from the csv file Iris and call it df.
df = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")

#I make the x axis the species axis.
x = df.species

#I make the y axis the Petal Length axis.
y = df.petal_length

#I call the plot scatter function for the x and y axis.
plt.scatter(x, y)

#This gives the plot diagram a title and says what size that title should be in this case 15. 
title = ("Comparing the Petal Lengths")
plt.title(title, fontsize=15)

#and displays the diagram to the user.
plt.show()

#Reference:https://ourcodingclub.github.io/2018/04/18/pandas-python-intro.html#following
#Laura Brogan 19/04/2019