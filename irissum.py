# Initial Python Code to Just get the first ten lines of the data set returned to screen.
# To start I import pandas as pd
import pandas as pd

#Identify data as iris_data reading the csv file.
iris_data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")

#
summary = iris_data.describe()

summary = summary.transpose()

#Then I desplay the summary data  to the user. 
print(summary.head())

#Reference:https://raw.githubusercontent.com/RitRa/Project2018-iris/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.py

#Laura Brogan 19/04/2019