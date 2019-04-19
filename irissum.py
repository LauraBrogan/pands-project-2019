# This is to obtain a summary of the data contained in the iris data set, the .
# To start I import pandas as pd
import pandas as pd

#Identify data as iris_data reading the csv file.
iris_data = pd.read_csv ("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv")

#This gives descriptive statistics that summarise all samples take for the four categories, septal lenght, septal width, petal length, petal wedth
summary = iris_data.describe()

#The datat is transposed into a table format for the user. 
summary = summary.transpose()

#Then I dissplay the summary data to the user. 
print(summary.head())

#Reference:https://raw.githubusercontent.com/RitRa/Project2018-iris/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.py

#Laura Brogan 19/04/2019
