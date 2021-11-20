while True:
    try:
        #key，string分别代表输入的key的加要密的字符串
        #chars是密钥对应的字母表，res是要返回的结果。
        key, string, chars, res = input(), input(), [], ""
        #经过下面的循环，chars前面几个是密匙的字母
        for i in key:
            if i not in chars:
                chars.append(i)
        #如果输入的key中有小写字母，转为大写字母。
        chars = list(map(lambda c: c.upper(), chars))
        #剩下的字母，填充到chars里面。
        for i in range(65, 91):
            if chr(i) not in chars:
                chars.append(chr(i))
        # 将输入加密。
        for i in string:
            if i.isupper():
                res += chars[ord(i) - 65]
            elif i.islower():
                res += chars[ord(i) - 97].lower()
            else:
                res += i
        print(res)

    except:
        break
