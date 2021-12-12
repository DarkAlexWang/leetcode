# Python3 implementation to
# count total number of ways
# to split a string to get
# prime numbers
MOD = 1000000007

# Function to check whether
# a number is a prime number
# or not
def isPrime(number):

    num = int(number)
    i = 2

    while i * i <= num:
        if ((num % i) == 0):
            return False
        i += 1

    if num > 1:
        return True
    else:
        return False

# Function to find the count
# of ways to split string
# into prime numbers
def countPrimeStrings(number, i):

    # 1 based indexing
    if (i == 0):
        return 1
    cnt = 0

    # Consider every suffix
    # up to 6 digits
    for j in range(1, 7):

        # Number should not have
        # a leading zero and
        # it should be a prime number
        if (i - j >= 0 and
            number[i - j] != '0' and
            isPrime(number[i - j : i])):
            cnt += countPrimeStrings(number,
                                    i - j)
            cnt %= MOD

    # Return the final result
    return cnt

# Driver code
if __name__ == "__main__":

    s1 = "3175"
    l = len(s1)
    print (countPrimeStrings(s1, l))

# This code is contributed by Chitranayal
