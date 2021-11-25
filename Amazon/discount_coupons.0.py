def findCoupons(discounts):
    result = []
    for discount in discounts:
        stack = []
        for i in range(len(discount)):
            if stack and stack[-1] == discount[i]:
                stack.pop()
            else:
                stack.append(discount[i])
        if not stack:
            result.append(1)
        else:
            result.append(0)
    return result

print(findCoupons(["abba", "abca", "abbacbbc", "aabb", "xaaxybbyzccz", "vaas", "jay"]))
