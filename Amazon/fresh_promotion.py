# N: # of codeList
# M: # of items in shopping cart

# Time complexity: O(M)
# Space complexity : O(1)
def freshPromotion(codeList, shoppingCart):
    matched = 0
    cartIndex = 0
    for code in codeList:
        found = False
        while cartIndex < len(shoppingCart):
            if shoppingCart[cartIndex] != code[0] and shoppingCart[cartIndex] is not 'anything':
                cartIndex += 1
                continue
            cartIndex += 1
            codeIndex = 1
            while codeIndex < len(code) and cartIndex < len(shoppingCart):
                if code[codeIndex] != shoppingCart[cartIndex] \
                        and code[codeIndex] is not 'anything':
                    break
                codeIndex += 1
                cartIndex += 1
            if codeIndex == len(code):
                found = True
                break
        if found:
            matched += 1
        if cartIndex == len(shoppingCart):
            break
    return matched == len(codeList)


if __name__ == '__main__':
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == True
    assert freshPromotion([['orange', 'apple', 'apple'], ['banana', 'apple', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['banana', 'orange', 'banana', 'apple', 'apple']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']) \
           == False
    assert freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['apple', 'apple', 'apple', 'banana']) \
           == False
    print(freshPromotion([['apple', 'apple'], ['banana', 'anything', 'banana']],
                          ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
