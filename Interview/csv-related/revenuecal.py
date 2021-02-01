# reading FS sheet and calculate revenue
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# plot config
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

filename = 'FSsheet2020.csv'

if os.path.exists(filename):
    df = pd.read_csv(filename, sep=',', error_bad_lines = False)
    df.drop(df.index[[0, 1, 2, 3, 4]], inplace = True)
    df.rename(columns = {'Unnamed: 0':'Date', 'Unnamed: 1':'Job Number'}, inplace=True)
    new_df = df[['Date', 'Job Number', 'Company - Name', 'Due date', 'Date out', 'Engineer', 'Description of samples', 'Hours']]
    new_df['Hours'].fillna(value = 1, inplace=True)
    new_df['Company - Name'].dropna()
    #pd.set_option('display.max_columns', 10)
    print(new_df[:5])

new_df['Engineer'].value_counts()
#df_wrong = df[df['Company - Name'].str.contains('-')]
#pd.set_option('display.max_rows', 1000)
#print(df['Company - Name'])
new_df[['Company', 'Customer']] = df['Company - Name'].str.split("-", expand = True)
print(new_df[:5])
company_rank = new_df['Company'].value_counts().index.tolist()
#top_five = []
#for i in range(5):
#    top_five.append(comapy_rank[i])
#print(*[name for name in top_five], sep = '\n')
#
#
#new_df['Date'] = pd.to_datetime(new_df['Date'])
#new_df = new_df.set_index(new_df['Date'])
#performance = new_df.loc['1/01/2021':'2/01/2021']
#performance
