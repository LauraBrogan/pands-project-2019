#import pandas as pd
#import holo
#import csv
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib

#df = pd.read_csv('irisdataset.csv')

#df.shape

import pandas as pd
import numpy as np
#import holoviews as hv
import seaborn as sns
#hv.extension('bokeh', 'matplotlib')

df = pd.read_csv('irisdataset.csv')
df.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']


df['species'].unique()
print(df.groupby('species').size())



















#print(df('species').size())