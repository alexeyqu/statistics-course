import survey
import numpy as np
from collections import defaultdict
import operator
import matplotlib.pyplot as plt

min_on_time = 38
max_on_time = 40

def prob_birth(lst):
	num_early = sum([i for i in lst if int(i) < min_on_time])
	num_on_time = sum([i for i in lst if min_on_time <= int(i) <= max_on_time])
	num_late = sum([i for i in lst if int(i) > max_on_time])
	total = num_early + num_on_time + num_late
	return num_early / total, num_on_time / total, num_late / total

if __name__ == '__main__':
	table = survey.Pregnancies()
	table.ReadRecords('./data')
	df = table.ConvertToDataFrame()
	df_all_live = df[df['outcome'] == 1]
	df_first = df_all_live[df_all_live['birthord'] == 1]
	df_other = df_all_live[df_all_live['birthord'] != 1]

	prob_all = np.array(prob_birth(df_all_live['prglength']))
	prob_other = np.array(prob_birth(df_other['prglength']))
	prob_first = np.array(prob_birth(df_first['prglength']))
	print('Probabilities of being born (early, on time, late):')
	print('{0} (all live births)'.format(prob_all))
	print('{0} (first births)'.format(prob_first))
	print('{0} (other births)'.format(prob_other))
	print('{0} (first / other: relative risk)'.format(prob_first / prob_other))