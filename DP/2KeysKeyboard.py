import math 
 
# Method to find the divisors
def findDivisors(n) :
    l1 = [1]
    for i in range(2, int(math.sqrt(n) + 1)) :
        if (n % i == 0) : 
            # Check if divisors are equal
            if (n / i == i) :
                l1.append(i)
            else :
                l1 += [i, n//i]
                break
    return l1[-1]


class Solution:
    def __init__(self):
        self.mp = {1:0}
        self.steps = []

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
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
    sol = Solution()
    sol.minStepsUtil(343)        
        