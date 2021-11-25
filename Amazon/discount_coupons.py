def findCoupons(discounts):
    result = []
    for discount in discounts:
        if discount[0] == discount[-1]:
            discount = discount[1:-1]
        result.append(1 if finddiscountPattern(discount)else 0)
    return result

def finddiscountPattern(discount):
    mostleft = 0
    left = 1
    while left < len(discount):
        if discount[mostleft] == discount[left]:
            discount = discount[:mostleft]+discount[left+1:]
            mostleft = 0
            left = 1
        else:
            mostleft += 1
            left += 1
    if not len(discount):
        return True
    return False

print(findCoupons(["abba", "abca", "abbacbbc", "aabb", "xaaxybbyzccz", "vaas", "jay"]))
