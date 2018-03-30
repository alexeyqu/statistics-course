import matplotlib.pyplot as plt
import numpy as np

def pmf_classes():
	bin_size = 4
	classes = {5: 8, 10: 8, 15: 14, 20: 4, 25: 6, 30: 12, 35: 8, 40: 3, 45: 2}

	def mean(classes):
		return sum([(k + bin_size // 2) * v for k, v in classes.items()])

	def normalize(classes):
		total = sum(classes.values())
		for k, v in classes.items():
			classes[k] /= total
		return classes

	def pov_dean(classes):
		classes = normalize(classes)
		print("Mean by dean: {0}".format(mean(classes)))
		return classes

	def pov_students(classes):
		for k, v in classes.items():
			classes[k] *= k + bin_size // 2
		classes = normalize(classes)
		print("Mean by students: {0}".format(mean(classes)))
		return classes

	def unbias(classes):
		for k, v in classes.items():
			classes[k] /= k + bin_size // 2
		classes = normalize(classes)
		print("Mean unbiased: {0}".format(mean(classes)))
		return classes

	plt.bar(np.fromiter(classes.keys(), dtype=float) + bin_size // 2 - 0.2, list(pov_dean(classes).values()), width=0.2, align='center')
	plt.bar(np.fromiter(classes.keys(), dtype=float) + bin_size // 2 + 0.2, list(pov_students(classes).values()), width=0.2, align='center')
	plt.bar(np.fromiter(classes.keys(), dtype=float) + bin_size // 2, list(unbias(classes).values()), width=0.2, align='center')
	plt.show()

if __name__ == '__main__':
	pmf_classes()