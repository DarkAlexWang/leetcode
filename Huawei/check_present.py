#
#
#一公司使用字符串来记录考勤，首行输入的数字代表接下来需要判断的员工数，后面每一行代表一个员工的出勤记录，每行不超过10000个字符，每个单词代表每天的出勤情况，
#
#present代表正常出勤，absent代表缺席，late代表迟到，leaveearly代表早退，单词之间用空格隔开。
#如下所示： present present present
#
#现需要判断每个员工是否能获得全勤奖， 获得全勤奖的规则是：缺勤不超过1次，没有连续的迟到/早退，
#任意连续7天内出现缺勤/迟到/早退的次数不超过3次。
#
#输出要求：结果输出为一行，以空格隔开
#
#示例1：
#输入：
#2
#present
#present present
#
#输出：
#true true
#
#示例2：
#输入：
#3
#present
#absent present late present present present present leaveearly late present present
#
#输出：
#true true false
#
#其实就是一个逻辑判断，看你考虑的场景够不够全面

s1 = "present"
s2 = "absent present late present present present present leaveearly late present present"
s3 = "absent present late present present present present leaveearly present present"
s4 = "absent present late present present present present late leaveearly present present"
s5 = "absent present present present late present present leaveearly present present present late present"
s6 = "absent present present present present present present present late late"

def can_award(s1):
    l = s1.split(' ')
    if s1.count('absent') > 1:

        return 'False'
    if s1.count('late leaveearly') > 0 or s1.count('leaveearly late') >0 \
            or s1.count('late late') > 0 or s1.count('leaveearly leaveearly') > 0:
                return 'False'
    for i in range(len(l)):
        this - l[i]
        if this == 'absent' or this == 'late' or this == 'leaveearly':
            c = 0
            l1 = l[i + 1: i + 7]
            print(l1)
            c += l1.count('absent')
            c += l1.count('late')
            c += l1.count('leaveearly')
            print(c)
            if c > 2:
                return 'False'
    return 'True'

import sys

n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    line = sys.stdin.readline().strip()
    print(line)
    l.append(can_award(line))
print(' '.join(l))
