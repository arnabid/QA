# program to find all the primes less than or equal to n

def sieveEratosthenes(n):
	prime = [True] * (n+1)
	p = 2
	while (p*p <= n):
		if prime[p]:
			for i in range(2*p, n+1, p):
				prime[i] = False
		p += 1

	# print all the primes
	for p in range(2, n+1):
		if prime[p]:
			print (p, end = ",")
	print ("")


if __name__ == '__main__':
	sieveEratosthenes(2)