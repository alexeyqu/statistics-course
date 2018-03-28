import survey
import numpy as np

table = survey.Pregnancies()
table.ReadRecords('./data')

df = table.ConvertToDataFrame()

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