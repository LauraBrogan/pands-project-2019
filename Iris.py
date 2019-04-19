#Initial Python Code to Just get the first ten lines of the data set returned to screen.
#To start I import pandas as pd

import pandas as pd

#Identify data as pandas reading the csv file.
data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")

#Identify Data To as the data head for 10 line.
data_top = data.head(10) 

#Then I desplay the data top to the user. 

print(data_top) 

#Reference:https://www.geeksforgeeks.org/python-pandas-dataframe-series-head-method/

#Laura Brogan 19/04/2019