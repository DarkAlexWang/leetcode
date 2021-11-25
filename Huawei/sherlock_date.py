import sys

#strings = []
#for i in range(4):
#    line = sys.stdin.readline().strip()
#    values = list(map(str, line.split()))
#    for string in values:
#        strings.append(string)
strings = ['3485djDkxh4hhGE',
        '2984akDfkkkkggEdsb',
        's&hgsfdk',
        'd&Hyscvnm'
        ]
s1 = strings[0]
s2 = strings[1]
s3 = strings[2]
s4 = strings[3]
print(s1, s2)

week = ['MON', "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
flag = 0
length1 = len(s2) if len(s1) > len(s2) else len(s1)

for i in range(length1):
    if s1[i] == s2[i] and (ord(s1[i]) >= 65 and ord(s1[i]) <= 71) and flag == 0:
        flag = 1
        print(week[ord(s1[i]) - 65] + ' ')
        i += 1
    if flag == 1 and s1[i] == s2[i]:
        if s1[i] >= '0' and s1[i] <= '9':
            print("0" + chr(a[i] - '0') + ':')
            break
        if s1[i] >= 'A' and s1[i] <= 'N':
            print(chr(ord(s1[i]) - 65 + 10) + ":")
            break

length2 = len(s4) if len(s3) > len(s4) else len(s3)

for i in range(length2):
    if s3[i] == s4[i] and (ord(s3[i]) >= 65 and ord(s3[i]) <= 90) or (ord(s3[i]) >= 97 and ord(s3[i]) <= 122):
        if i <= 9:
            print("0" + chr(i))
            break
        else:
            print(chr(i))
            break
