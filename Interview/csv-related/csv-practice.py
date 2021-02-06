import csv
import pandas as pd
import os
import re

filename = ('FSsheet2021.csv')
if os.path.exists(filename):
    df = pd.read_csv(filename, sep=',', error_bad_lines = False, names = ['Date', 'Engineer'])
    df[df.Engineer == 'ZW']
    df[''].dropna()
    df.drop([], inplace=True)
    df.rename(columns = {:}, inplace = True)
    new_df = df['Date']
    new_df = df[].copy()
    new_df = df.loc[][].apply()
    new_df['Engineer'].value.counts()
    company_rank = new_df['Company'].value_counts().index.tolist()
    top_five = []
    for i in range(5):
        top.five.append(company_rank[i])
    print(*[name for name in top_five], sep='\n')

    new_df['Date'] = pd.to_datetime(new_df['Date'])
    new_df = new_df.set_index(new_df['Date'])
    performance = new_df.loc['1/01/2021':'1/14/2021']


    df_p['Hours'] = df_p['Hours'].apply(lambda x: x.replace('S', '')).replace('hrs so far', '')
                if isinstance(x, str) else x).astype(float)

    df_p['Hours'].replace(to_place='[^0-9]+', value='', inplace=True, regex=True)
    df_p['Hours'] = df_p['Hours'].apply(lambda x: x*500 if x > 30 else x)

    df_p['rank'] = df_p.groupby['Engineer']['Hours'].rank["dense", ascending= True]
    df_p.groupby['Engineer'].agg['mean', 'count', 'sum']
    df_by_week = df_by_week.groupby(['Engineer', pd.Grouper(key = 'Date', freq= 'W-MON')])['Hours'].sum().reset_index().sort_value('Date')

    group = df.groupby('group1')
    group.agg([len, sum])
    group = df.groupby('labels')['value']
    df['value.sum'] = group.transform('sum')
    df['MonthNumber'] = df['col1'].apply(lambda x : x.month)
    df['MonthName'] = df['col1'].apply(lambda x: x.strftime('%B'))
    df['col3'] = df['col2']*df['col1'].apply(lambda x: -1 if x == 'minus' else (1 if x == 'positive' else np.nan))
    df1.add(df2, fill_value = 0)
    def Half(x):
        return x.sum()
    df['new'] = group['value1'].tranform(Half)
    newcol = group['value1'].agg([Harf, HalfPlus])
    df.merge(newcol, left_on['group1', 'group2'], right_index = True)

def printBipedalDinosaursOrderBySpeed(filePathDinoInfo, filePathAddInfo):
    bipedalDinosaurs = {}
    g = 9.8

    with open(filePathAddInfo, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline().strip()
            if line:
                NAME, STRIDE_LENGTH, STANCE = line.split(',')
                if STANCE == "bipedal":
                    bipedalDinosaurs[NAME] = float(STRIDE_LENGTH)

    with open(filePathDinoInfo, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline().strip()
            if line:
                NAME, LEG_LENGTH, DIET = line.split(',')
                if NAME in bipedalDinosaurs:
                    STRIDE_LENGTH, LEG_LENGTH = bipedalDinosaurs[NAME], float(STRIDE_LENGTH)
                    bipedalDinosaurs[NAME] = ((STRIDE_LENGTH/ LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
    heap = [(value, key) for key, value in bipedalDinosaurs.items()]
    fastest = heapq.nlargest(len(heap), heap)
    print(*[name for speed, name in fastest], sep = '\n')

printBipedalDinosaursOrderBySpeed('dataset1.csv', 'dataset2.csv')

#Team Orca is responsible for patrolling and responding to actions by bad actors attacking zendesk. We need your help to sort through the data and identify these different sets of bad and good actors. We have a dump of logs in CSV format that show various different actors doing bad things with zendesk accounts. Write code to help identify these suspicious accounts.
#
#Tasks:
#Identify:
#-a list and count of how many accounts we have in the logs.
#-a list of how many accounts have done X action ( e.g. API key created, subgroups )
#-which accounts have done multiple actions
#-The suspicious accounts
#-The good accounts
#
#
#Example of a bad event:
#If eventA (account_creation) and eventB(API_key_created) occur within 5 minutes of each other we can assume that this is a bad actor.
#
#E.g.:
#Account_id, customer_ip, timestamp, event_type
#43526, 192.25.0.4, 2020-11-19T10:22:53Z, account_creation
#43526, 22.168.0.4, 2020-11-19T10:26:53Z, api_key_created
#
#Or the same IP creating multiple accounts:
#Account_id, customer_ip, timestamp, event_type
#56455, 192.25.0.4, 2020-11-19T10:22:53Z, account_creation
#15485, 192.25.0.4, 2020-11-19T10:22:54Z, account_creation
#98785, 192.25.0.4, 2020-11-19T10:22:55Z, account_creation
#84546, 192.25.0.4, 2020-11-19T10:22:56Z, account_creation
#13431, 192.25.0.4, 2020-11-19T10:22:57Z, account_creation
#
#https://app.coderpad.io/resources/docs/custom-files/accessing-files
import pandas as pd
import os
import csv
import collections
from datetime import datetime

class Solution:
    def csv_reader(self, filePath):
        if os.path.exists(filePath):
            df = pd.read_csv(filePath, sep=',')
            print(df)
            return df

    def account_num(self, df):
        print(df['account_id'].value_counts())
        account_list = []
        account_rank = df['account_id'].value_counts().index.tolist()
        for i in range(len(account_rank)):
            account_list.append(account_rank[i])
        print(*[account for account in account_list], sep='\n')
        return account_list


    def suspicious_account(self, df):
        #df = pd.to_datetime(df['timestamp'])
        bad_account_dic = collections.defaultdict(list)
        res = []
        with open(filePath, 'r') as f:
            line = f.readline()
            while line:
                line = f.readline().strip()
                if line:
                    account_id, customer_ip, timestamp, event_type = line.split(',')

                    fmt = '%Y-%m-%dT%H:%M:%SZ'
                    timestamp = datetime.strptime(timestamp, fmt)
                    if event_type == 'account_creation':
                        bad_account_dic[customer_ip].append(account_id)
            #print()
            for key, values in bad_account_dic.items():
                if len(values)  >= 2:
                    res.append(key)
        print(res)

        #df['time_rank'] = df['']
        #print(df['Date'])

        #print(df['customer_ip'].value_counts())
        #df['Bad'] = df.groupby(['customer_ip', 'account_id'])

if __name__ == '__main__':
    solution = Solution()
    filePath = '/home/coderpad/data/shuffled_data_refreshed.csv'
    df = solution.csv_reader(filePath)
    #solution.account_num(df)
    solution.suspicious_account(df)



 account_id  customer_ip             timestamp           event_type
0        84546   192.25.0.4  2020-11-19T10:22:56Z     account_creation
1        56455   192.25.0.4  2020-11-19T10:22:53Z     account_creation
2        43526    2.168.0.4  2020-11-19T10:26:53Z      api_key_created
3        12314   134.25.0.4  2020-11-19T10:23:53Z      api_key_created
4        56455    2.168.0.4  2020-11-19T10:26:53Z      api_key_created
5        56455    2.168.0.4  2020-11-19T10:26:53Z  talk_number_created
6        12562    3.168.0.1  2020-11-19T10:15:53Z     account_creation
7        12345  192.168.0.1  2020-11-19T10:15:53Z     account_creation
8        12314   134.25.0.4  2020-11-19T10:22:53Z     account_creation
9        54343  192.563.0.4  2020-11-19T10:22:53Z      api_key_created
10       12345  192.168.0.1  2020-11-19T10:19:53Z      api_key_created
11       12537      5.3.0.4  2020-11-19T10:22:53Z     account_creation
12       56455    2.168.0.4  2020-11-19T10:26:53Z  talk_number_created
13       13423    192.3.0.4  2020-11-19T12:22:53Z     account_creation
14        6584    192.3.2.1  2020-11-19T10:15:53Z     account_creation
15       65745  213.168.0.4  2020-11-19T10:22:53Z     account_creation
16       43526   192.25.0.4  2020-11-19T10:22:53Z     account_creation
17       54343    3.168.0.1  2020-11-19T10:15:53Z     account_creation
18       42542   134.25.0.4  2020-11-19T10:22:53Z     account_creation
19       56455    2.168.0.4  2020-11-19T10:26:53Z  talk_number_created
20       13413     10.2.0.4  2020-11-19T16:28:53Z      api_key_created
21       42542   134.25.0.4  2020-11-19T10:23:53Z      api_key_created
22       23452     25.8.0.1  2020-11-19T10:15:53Z     account_creation
23       62546   15.168.0.1  2020-11-19T10:15:53Z     account_creation
24       98656   43.342.0.1  2020-11-19T10:15:53Z     account_creation
25       76863   134.25.0.4  2020-11-19T10:22:53Z     account_creation
26       65745  213.168.0.4  2020-11-19T10:30:53Z      api_key_created
27      780556  547.168.0.1  2020-11-19T10:15:53Z     account_creation
28       13431   192.25.0.4  2020-11-19T10:22:57Z     account_creation
29       15646   17.168.0.4  2020-11-19T10:26:50Z     account_creation
30       54373    3.168.0.1  2020-11-19T10:15:53Z     account_creation
31       15485   192.25.0.4  2020-11-19T10:22:54Z     account_creation
32       13413     10.2.0.4  2020-11-19T16:28:53Z  talk_number_created
33       98785   192.25.0.4  2020-11-19T10:22:55Z     account_creation
34       13413     10.2.0.4  2020-11-20T16:22:53Z     account_creation
35       56455    2.168.0.4  2020-11-19T10:26:53Z  talk_number_created
36       12537      5.3.0.4  2020-11-19T10:22:53Z  talk_number_created
37       74689     24.9.0.1  2020-11-19T10:15:53Z     account_creation
38       56455   192.25.0.4  2020-11-19T10:22:53Z     account_creation
39       12345  192.168.0.4  2020-11-19T10:22:53Z      api_key_created
40       76863   134.25.0.4  2020-11-19T10:24:53Z      api_key_created
