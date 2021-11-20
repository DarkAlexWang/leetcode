#
#
#题目：两次输入，各输入一行小写字母构成的字符串，要求从第一次输入的字符串中找出第二行字符串中有的，按照ascii编码排序,
#最终输出没有重复字母的字符串。
#
#示例：
#输入：
#bacha
#bbaaccedfg
#
#输出：
#abc
#
#解题思路：
#几乎就是字符串的基本操作，没啥好说的

s = input()
s2 = input()
s1 = ''

for i in s:
    if s2.count(i) > 0:
        if i in s1:
            pass
        else:
            s1 += i

s1 = ''.join(sorted(s1))
print(s1)
