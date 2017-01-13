"""
reference: https://www.hackerrank.com/challenges/candies
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    for _ in xrange(n):
        arr.append(int(raw_input()))

    candies = [0] * n
    candies[0] = 1
    for i in xrange(1,n):
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1] + 1
        else:
            candies[i] = 1
    
    total = candies[n-1]
    for i in xrange(n-2,-1,-1):
        if arr[i] > arr[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1
        total += candies[i]
    print (total)
