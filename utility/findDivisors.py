
# returns the list of divisors of n in sorted order
def findDivisors(n):
	i = 1
	l1, l2 = [], []
	while i * i <= n:
		if n % i == 0:
			if i == n//i:
				l1.append(i)
			else:
				l1.append(i)
				l2.append(n//i)
		i += 1
	l1 += l2[::-1]
	print (l1)

if __name__ == '__main__':
	n = 31
	findDivisors(n)

