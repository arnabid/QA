"""
leetcode 140. Word Break II
reference: https://leetcode.com/problems/word-break-ii/description/
"""


dictionary = set(["cat", "sand", "cats", "dog", "and"])
stacks = []
valid = set()
nvalid = set()

def dfs(s, index, n, stack):
    if index == n:
        stacks.append(list(stack))
        valid.update(stacks[-1])
        stack.pop()
        return
    if index in nvalid:
    	stack.pop()
    	return
    for i in range(index+1, n+1):
        t = s[index:i]
        if t in dictionary:
            stack.append(i)
            dfs(s, i, n, stack)
    if index not in valid:
    	nvalid.add(index)
    stack.pop()

if __name__ == '__main__':
    s, output = "catsanddog", []
    n = len(s)
    stack = [0]
    dfs(s, 0, n, stack)
    for stack in stacks:
        output.append(" ".join(s[stack[k-1]: stack[k]] for k in range(1,len(stack))))
    print (output)
