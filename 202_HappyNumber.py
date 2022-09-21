
def isHappy(n):
    # base case
    if n == 1:
        return True
    # recursive case
    else:
        try:
            nlist = [int(num) for num in str(n)]
            number = 0
            for i in nlist:
                number += (i ** 2)
            n = number
            return isHappy(n)
        except RecursionError:
            return False


print(isHappy(116))
