"""
reference: https://www.hackerrank.com/challenges/minimum-time-required/problem
"""

def minTime(machines, goal):
    l = goal * min(machines) // (len(machines))
    h = min(machines) * goal
    
    def possible(k):
        return sum(math.floor(k/m) for m in machines) >= goal
    
    while l <= h:
        ans = l + (h-l)//2
        if possible(ans):
            h = ans - 1
        else:
            l = ans + 1
    return l
