# function to check if a number is prime

def isPrime(N):
	if N <= 1:
		return False

	i = 2
	while i * i <= N:
		if N % i == 0:
			return False
		i += 1
	return True

if __name__ == '__main__':
	print (isPrime(131))