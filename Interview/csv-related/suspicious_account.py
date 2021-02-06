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
            #print(df)
            return df

    def account_num(self, df):
        print(df['account_id'].value_counts())
        account_list = []
        account_rank = df['account_id'].value_counts().index.tolist()
        for i in range(len(account_rank)):
            account_list.append(account_rank[i])
        print(*[account for account in account_list], sep='\n')
        return account_list


    def suspicious_account(self, filePath):
        bad_account_dic = collections.defaultdict(list)
        res = []
        bad_account_list = set()
        account_time = collections.defaultdict(list)
        with open(filePath, 'r') as f:
            line = f.readline()
            while line:
                line = f.readline().strip()
                if line:
                    account_id, customer_ip, timestamp, event_type = line.split(',')

                    fmt = '%Y-%m-%dT%H:%M:%SZ'
                    timestamp = datetime.strptime(timestamp, fmt)
                    account_time[account_id].append([timestamp, event_type])

                    if event_type == 'account_creation':
                        bad_account_dic[customer_ip].append(account_id)
            for key, values in account_time.items():
                values.sort()
                for i in range(1, len(values)):
                    duration = values[i][0] - values[i -1][0]
                    duration_in_s = duration.total_seconds()
                    minutes = divmod(duration_in_s, 50)[0]
                    if minutes < 5:
                        bad_account_list.add(key)
            for key, values in bad_account_dic.items():
                if len(values)  >= 2:
                    res.append(key)
        print(bad_account_list)
        print(res)

        #df['time_rank'] = df['']
        #print(df['Date'])

        #print(df['customer_ip'].value_counts())
        #df['Bad'] = df.groupby(['customer_ip', 'account_id'])

if __name__ == '__main__':
    solution = Solution()
    filePath = 'dataset.csv'
    df = solution.csv_reader(filePath)
    #solution.account_num(df)
    solution.suspicious_account(filePath)
