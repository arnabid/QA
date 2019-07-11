import math
from matplotlib import pyplot as plt
 
# Method to find the second largest divisor of n 
def findDivisors(n) :
    i = 2
    while i * i <= n:
        if n % i == 0:
            return n//i
        i += 1
    return 1


# Solution class
class Solution:
    def __init__(self):
        self.mp = {1:0}
        self.steps = []

    def minSteps(self, n):
        """
        #:type n: int
        #:rtype: int
        """
        self.steps.append(n)
        if n in self.mp:
            return self.mp[n]
        d = findDivisors(n)
        ans = n//1
        if d in self.mp:
            ans = min(ans, n//d + self.mp[d])
        else:
            ans = min(ans, n//d + self.minSteps(d))
        self.mp[n] = ans
        return ans

    def minStepsUtil(self, n):
        ans = self.minSteps(n)
        print ("The minimum number of steps = {}".format(ans))
        self.steps.append(1)
        print (self.steps[::-1])

if __name__ == '__main__':
    #print (findDivisors(20))
    x = range(1,101)
    sol = Solution()
    y = []
    for ix in x:
        sol = Solution()
        y.append(sol.minSteps(ix))
    print (y)
    plt.plot(y, x)
    plt.show()


        