#
#
#题目：假设书本的叠放有这样的规则，当A书的长度和宽度都大于B书时，可以将其B书置于A的上方，堆叠摆放，请设计一个程序，根据输入的书本长宽，计算最多可以堆叠摆放多少本书？

#示例：这里代表有3本书，第1本长宽分别为16和15，第2本长宽为13和12，第3本长宽为15和14。
#输入：
#[[16,15], [13, 12], [15, 14]]
#
#输出：
#3
#
#解题思路：
#1、先处理好输入的字符串，转成python的列表
#2、列表内嵌列表，可以考虑转成字典并按键排好序，方便快速比较

s = '[[16, 15], [16, 14], [13, 12], [15, 14]]'

s = s.replace(' ', '')
s = s.replace('],[', '];[')
l = s[1:-1].split(';')

d = {}
for i in l:
    if i[1:-1].split(',')[0] in d.keys():
        d[i[1:-1].split(',')[0]] = int(i[1:-1].split(',')[1]) if int(i[1:-1].split(',')[1]) >= d[i[1:-1].split(',')[0]] \
                else d[i[1:-1].split(',')[0]]
    else:
        d[i[1:-1].split(',')[0]] = int(i[1:-1].split(',')[1])

print(d)
d2 = {}

for j in sorted(d, reverse = True):
    d2[j] = d[j]

keys = list(d2.keys())

print(keys)
c = 0
for k, v in d2.items():
    k_index = keys.index(k)
    for i in keys[k_index +1::]:
        if v > d2[i]:
            c += 1
print(c)
