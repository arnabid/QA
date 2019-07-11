import numpy as np 
import matplotlib.pyplot as plt 

if __name__ == '__main__':
	x = np.array(range(1000000))
	y1 = 2*x - 2
	y2 = 3*(x/2)

	plt.plot(x, y1, y2)
	plt.title("Finding simultaneous min and max")
	plt.xlabel("n")
	plt.ylabel("T(n)")
	plt.show()
