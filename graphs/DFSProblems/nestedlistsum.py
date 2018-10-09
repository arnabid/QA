"""
reference: https://www.leetfree.com/problems/nested-list-weight-sum-ii.html
"""

total = [0]
mnlevel = [0]

# find the depth of the recursion
def processdepth(lst, level):
	mnlevel[0] = max(mnlevel[0], level)
	for elem in lst:
		if type(elem) is list:
			processdepth(elem, level+1)

# find the nested list weighted sum
def process(lst, level):
	for elem in lst:
		if type(elem) is list:
			process(elem, level-1)	
		else:
			total[0] += elem*level


if __name__ == '__main__':
	#lst = [1,[4,[6]]]
	#lst = [[1,1],2,[1,1]]
	lst = [1,[4, [6], [5, [2]]]]
	processdepth(lst, 1)
	print (mnlevel[0])
	process(lst, mnlevel[0])
	print (total[0])
