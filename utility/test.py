
i = 3
N = 100
while i * i <= N:
	while N % i == 0:
		print (i)
		N = N // i
	i += 2
