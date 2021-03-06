import survey
import numpy as np
from collections import defaultdict
import operator
import matplotlib.pyplot as plt
import pandas as pd
import random


def chapter_1(df):
	'''
	ThinkStats Chapter 1 solutions
	'''
	# task 1: number of pregnancies
	print('Number of pregnancies: {0}'.format(len(df))) 

	# task 2: total of live births
	print('Number of live births: {0}'.format(sum(df[df['outcome'] == 1]['outcome'])))

	# task 3: total of live births splitted for first babies and other babies
	df_first = df[df['birthord'] == 1]
	df_other = df[df['birthord'] != 1]
	print('Number of live births: {0} (1st baby), {1} (non-1st baby)'.format(
		sum(df_first[df_first['outcome'] == 1]['outcome']), 
		sum(df_other[df_other['outcome'] == 1]['outcome'])))

	# task 4: avg pregnancy length for first babies and other babies
	prglength_first = np.mean(df_first[df_first['outcome'] == 1]['prglength'])
	prglength_other = np.mean(df_other[df_other['outcome'] == 1]['prglength'])
	print('Average pregnancy length (in weeks): {0} (1st baby) {2} {1} (non-1st baby)'.format(
		prglength_first, prglength_other, '>' if prglength_first > prglength_other else '<'))
	delta = abs(prglength_first - prglength_other)
	print('Delta: {0} (weeks), {1} (hours)'.format(delta, delta * (24 * 7)))


def make_hist(lst, trim=False):

	def reject_outliers(data, m=2):
	    return data[abs(data - np.mean(data)) < m * np.std(data)]
	
	if trim:
		lst = reject_outliers(lst)
	hist = defaultdict(int)
	for item in lst:
		hist[item] += 1
	return hist


def mode(hist):
	return max(hist.items(), key=operator.itemgetter(1))[0]


def all_modes(hist):
	return sorted(hist.items(), key=operator.itemgetter(1), reverse=True)


def chapter_2(df):
	'''
	ThinkStats Chapter 2 solutions
	'''
	df_first = df[df['birthord'] == 1]
	df_other = df[df['birthord'] != 1]
	print('Gestation time (mean, std deviation): \n{0} (first baby), \n{1} (non-1st baby)'.format(
		(np.mean(df_first[df_first['outcome'] == 1]['prglength']), df_first[df_first['outcome'] == 1]['prglength'].std()),
		(np.mean(df_other[df_other['outcome'] == 1]['prglength']), df_other[df_other['outcome'] == 1]['prglength'].std())))

	# show histogram of all prglengths for 2 df
	hist = make_hist(df_first[df_first['outcome'] == 1]['prglength'], True)
	print(mode(hist))
	print(all_modes(hist))

	hist_other = make_hist(df_other[df_other['outcome'] == 1]['prglength'], True)
	plt.bar(np.fromiter(hist.keys(), dtype=float) - 0.2, list(hist.values()), width=0.2, align='center')
	plt.bar(np.fromiter(hist_other.keys(), dtype=float) + 0.2, list(hist_other.values()), width=0.2, align='center')
	plt.show()


def make_cdf(hist):
	cdf = defaultdict(int)
	total = 0
	for k in sorted(hist.keys()):
		total += hist[k]
		cdf[k] = total
	return cdf


def chapter_4(df):
	'''
	ThinkStats chapter 4 solutions
	'''
	df_first = df[df['birthord'] == 1]
	df_other = df[df['birthord'] != 1]
	wgt_first = df_first[df_first['totalwgt_oz'] != 'NA']['totalwgt_oz']
	wgt_other = df_other[df_other['totalwgt_oz'] != 'NA']['totalwgt_oz']

	hist_first = make_hist(wgt_first)
	hist_other = make_hist(wgt_other)

	# plt.bar(np.fromiter(hist_first.keys(), dtype=float) - 0.2, list(hist_first.values()), width=0.4, align='center')
	# plt.bar(np.fromiter(hist_other.keys(), dtype=float) + 0.2, list(hist_other.values()), width=0.2, align='center')
	# plt.show()

	cdf_first = make_cdf(hist_first)
	cdf_other = make_cdf(hist_other)

	plt.plot(np.fromiter(cdf_first.keys(), dtype=float) - 0.2, list(cdf_first.values()))
	plt.plot(np.fromiter(cdf_other.keys(), dtype=float) + 0.2, list(cdf_other.values()))
	plt.show()


def random_study():
	n = 1000
	sample = [random.random() for _ in range(n)]
	
	hist = make_hist(sample)
	cdf = make_cdf(hist)
	plt.plot(np.fromiter(hist.keys(), dtype=float), list(hist.values()))
	# plt.plot(np.fromiter(cdf.keys(), dtype=float), list(cdf.values()))
	plt.show()


if __name__ == '__main__':
	table = survey.Pregnancies()
	table.ReadRecords('./data')
	df = table.ConvertToDataFrame()
	random_study()