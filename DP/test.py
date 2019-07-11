import math

table = {0:0, 1:1}
divisors = {}

def findDivisors(n) :
    if n in divisors:
        return divisors[n]
    l1 = []
    for i in range(2, int(math.sqrt(n) + 1)) :
        if (n % i == 0) :
            l1.append(n//i)
    divisors[n] = l1
    return l1

def downToZero(n):
    #
    # Write your code here.
    if n in table:
        return table[n]
    ans = float('inf')
    if n-1 in table:
        ans = min(ans, table[n-1]+1)
    else:
        table[n-1] = downToZero(n-1)
        ans = min(ans, table[n-1]+1)
    divs = findDivisors(n)
    for div in divs:
        if div in table:
            ans = min(ans, table[div]+1)
        else:
            table[div] = downToZero(div)
            ans = min(ans, table[div]+1)
    table[n] = ans
    return table[n]


if __name__ == '__main__':
	print (downToZero(3))