# reading FS sheet and calculate revenue
import csv
import os

filename = 'FSsheet2021.csv'

fields = []
rows = []

if os.path.exists(filename):
    #with open(filename, 'r') as csvfile, open('temp.csv', "a+") as tmp:
    #    csvwriter = csv.writer(tmp, delimiter = ",")
    #    csvreader = list(csv.reader(csvfile, delimiter = ","))
    #    csvreader.pop(1)
    #    csvreader.pop(2)
    #    with open(filename, 'w') as out:
    #        writer = csv.writer(out, delimiter = ',')
    #        for row in csvreader:
    #            if row[0] in (None, "") and row[1] in (None, ""):
    #                row[0] = "Date"
    #                row[1] = "Job Number"
    #            if row[2] in (None, ""):
    #                continue
    #            else:
    #                writer.writerow(row[0:1] + row[2:3] + row[12:13])
    dic = {}

    with open(filename, 'r') as csvfile:
        line = csvfile.readline()
        while line:
            line = csvfile.readline().strip()
            if line:
                dates, companys, hours = line.split(',', 2)
                new_hours = float()
                for hour in hours:
                    if hour in (None, ''):
                        hour = float(2)
                        new_hours = hour
                        continue
                    else:
                        res = ''
                        for ch in hour:
                            print(ch)
                            if ch.isdigit():
                                res += ch
                        if res == "":
                            hour = float(1)
                        else:
                            hour = float(res)
                        #print(hour)
                    new_hours = hour

                #print(dates, companys, new_hours)
                if companys.find('Sungki') != -1 or companys.find('Guanxiong') != -1 or companys.find('Kyoung') != -1:
                    dic[dates] = new_hours
        print(dic)


        #fields = next(csvreader)

        #for row in csvreader:
        #    rows.append(row)

        #print("Total no. of rows: %d"%(csvreader.line_num))

        #for ind, line in enumerate(csvreader):
        #    if ind == 1 or ind == 2:
        #        continue
        #    else:
        #        csvwriter.writerow(line)
        #tmp.seek(0)
    #with open(filename, "w") as out, open('temp.csv', 'r') as tmp:
    #    reader = csv.reader(tmp, delimiter = ",")
    #    writer = csv.writer(out, delimiter = ",")
    #    for row in reader:
    #        writer.writerow(row)

#print('Field names are:' + ', '.join(field for field in fields))

#print('\nFirst 5 rows are:\n')
#for row in rows[:5]:
#    for col in row:
#        print("%10s"%col),
#    print('\n')
