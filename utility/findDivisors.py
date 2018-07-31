# returns the list of divisors of n in sorted order

def findDivisors(n):
	i, l1, l2 = 1, [], []
	while i * i <= n:
		if n % i == 0:
			l1.append(i)
			if i != n//i:
				l2.append(n//i)
		i += 1
	l1 += l2[::-1]
	print (l1)

if __name__ == '__main__':
	n = 0
	findDivisors(n)
