def combine(a, b, target):
    sumList = []
    for i in a:
        for j in b:
            sum_ = i + j
            if sum_ <= target:
                sumList.append(sum_)
    sorted(sumList, reverse = False)
    return sumList

def get_number_of_options(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    # combine 2 lists together and sort
    a = combine(priceOfJeans, priceOfShoes, dollars)
    b = combine(priceOfSkirts, priceOfTops, dollars)

    #Search
    left = 0
    right = len(b) - 1
    counts = 0

    while left < len(a) and right >= 0:
        sum_amount = a[left] + b[right]
        if sum_amount <= dollars:
            counts += right + 1
            left += 1
        else:
            right -= 1

    return counts


if __name__ == "__main__":
    ans = get_number_of_options([2, 3], [4], [2, 3], [1, 2], 10)
    print(ans)
