def divab(a, b):
	l, h = 1, a
	while l <= h:
		m = l + (h-l)//2
		if m * b == a:
			return m
		elif m * b > a:
			h = m - 1
		else:
			l = m + 1
	return -1

if __name__ == '__main__':
	print (divab(21, 7))