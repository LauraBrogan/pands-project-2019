# **Programming and Scripting Project 2019**
***********************************************
<p align="justify">This repository contains my project which will look at Ronald Fishers Iris Flower Data Set.  It will briefly introduce Ronald Fisher and the data set and it will investigate the data set using python scripts as detailed below. This project is for the Programing and Scripting Moudule at GMIT.
I commenced work on 24th March 2019 and complted the task by the due date of April 28th 2019.

I struggeld in the early days of the project trying to get python scripts to read athe csv file correctly. This kinda put me off the project a bit initially.  </p>

[See here for the Project Instructions 2019](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## Introduction

>*<p align="justify"> "R.A. Fisher was born in London on 17 February 1890, the son of a fine-art auctioneer. His twin brother was stillborn. At Harrow School he distinguished himself in mathematics, despite being handicapped by poor eyesight which prevented him working by artificial light. His teachers used to instruct by ear, and Fisher developed a remarkable capacity for pursuing complex mathematical arguments in his head. This manifested itself in later life in his ability to reach a conclusion whilst forgetting the argument; to handle complex geometrical trains of thought; and to develop and report essentially mathematical arguments in English (only for students to have to reconstruct the mathematics later)."*

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). The data set contains 150 observation of the Iris flowers. Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. The fifth column is the species of the flower observed. All observed flowers belong to one of three species.  The first four colums are numerical with one decimal place and a text column with the flower name.

Sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the
morphologic variation of Iris ﬂowers of three related species. Two of the three species were collected in the Gasp´e Peninsula ”all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”. </p>

## Summary of My Investigations
+ I found that using a python script I could get the data set displayed in the command line, I went with the first 10 lines of the data set but this can be changed to any amount of lines from the data set.

+ I plotted a scatter diagram to look at the petal lengths of the three Iris species, from this it is easy to see the the setosa has the smallest petal length and the virginica has the longest petal length and that there is not a huge difference between the petal lengths of the virginica and the versicolor.

+ Through summarising the data in the data set, looking at the mean, standard deviation, min, 25%, 50%, 70% and max of all species based on the sepal_lenth, sepal_width, petal_length and petal_width.  From the this summary, we can see there is a huge range in the size of the Sepal Length and Petal Length.

+ From the boxplot chart analysis, we can see there are clear differences in the size of the Sepal Length, among the different species. 

## What the Iris's Actually look like
These are images of the Iris Flowers for which the data set was created. 
![alt text](https://github.com/LauraBrogan/pands-project-2019/blob/master/Images%20of%20the%20Iris%20Species.jpg)

## Libaries used in this Project
I Imported: Pandas, Matplotlib, Seaborn.

* Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.

* Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.

* Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

## The Data Set CSV File
This is the csv file of the data set that I used for this project. 
Downloaded from [Here](https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv)
Saved locally as iris.csv

## My Repositiory can be download from git hub 
1. Go to Git Hub using the following link [Click Here:](https://github.com/LauraBrogan/pands-project-2019)
2. Click the download button

## Running the Code
For each of my Python Scripts you must:
1. Make sure you have python installed.
2. From the comand line interface open the folder pands-project-2019
3. To run each of the python files you must enter either:

        A. python iris.py 

        B. python plot.py 

        C. python irissum.py 

        D. python boxpl.py into the command line.

4. If the command displays a diagram you must close this first before you can run the next script.

## What Each File Contains:
###**A. iris.py**###

This file is a basic file to read the csv file and display to the user the top ten lines of the data set. 
I stated with a basic file like this as I was having a lot of difficulty trying to get my coding off the ground.  This is the result of running that script. 
![alt text](https://github.com/LauraBrogan/pands-project-2019/blob/master/iris.JPG)

It displays to us the first ten lines of the data set with the five column headings, sepal_length,  sepal_width,  petal_length,  petal_width, and species.

###**B. plot.py**###

This file contains the following code:
```python
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

#and display this to the user.
plt.show()

#Reference:https://ourcodingclub.github.io/2018/04/18/pandas-python-intro.html#following
#Laura Brogan 19/04/2019
```
It makes the data visual in a scatter plot diagram and it is clear to see that the petal length of the setosa is the smallest and the virginica has the largest petal length.

###**C. irissum.py**###

This is the outcome of running the above python script
![alt text](https://github.com/LauraBrogan/pands-project-2019/blob/master/irissum.JPG)

This script helps to summarise the data set we can see what the mean, min, max, standard deviations values are for the total data set under the headings sepal_length,  sepal_width,  petal_length,  petal_width,

###**D. boxpl.py**###

This pythons script produces a box plot which shows the distribution of the quantitative data for the sepal_length in a way that facilitates comparisons between variables. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution. This allows for the visualisation of the sepal length of each of the three Iris species.

## References:
I used GMIT Video Lectures by Ian McLoughlin and class notes to complete this work.
In addtion I searched on line using some of the following websites:

-[Springer Link](https://link.springer.com/referenceworkentry/10.1007%2F978-1-349-58802-2_581)

-[Report on Edgar Anderson’s Iris Data Analysis](https://www.academia.edu/13069408/Report_on_Edgar_Anderson_s_Iris_Data_Analysis)

-[Jstor](https://www.jstor.org/stable/2528392?read-now=1&seq=2#page_scan_tab_contents)

-[Matplotlib](https://matplotlib.org/)

-*Image* [Medium Basic Analysis of the Iris Data set Using Python](https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342)

-*Iris.py File* [Geeks for Geeks](https://www.geeksforgeeks.org/python-pandas-dataframe-series-head-method/)

-*Plot.py File* [Coding Club](https://ourcodingclub.github.io/2018/04/18/pandas-python-intro.html#following)

-*Irissum.py File* [Coding Git Hub](https://raw.githubusercontent.com/RitRa/Project2018-iris/master/Project%2B2018%2B-%2BFishers%2BIris%2Bdata%2Bset%2Banalysis.py)

-*Boxpl.py File* [Seaborn](https://seaborn.pydata.org/generated/seaborn.boxplot.html)

For each of the python scripts the specific references are commented in the code, with links to each of above sites which relate to that script. 

***Laura Brogan 20/04/2019*** 