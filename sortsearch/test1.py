def animal_counts(heads, legs):
	ans = {}
	for r in range(heads+1):
		c = heads - r
		if 4*r + 2*c == legs:
			ans['chickens'] = c
			ans['rabbits'] = r
			break
	return ans


if __name__ == '__main__':
	print (animal_counts(30, 80))

