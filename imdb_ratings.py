import pandas as pd
import os

url = 'https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv'

def get_data(url, save=False):
	df = pd.read_csv(url)
	
	if save:
		df.to_pickle('ratings.pickle')

	return df


def read_data():
	return 	pd.read_pickle('ratings.pickle')

if __name__ == '__main__':
	if not os.path.exists('ratings.pickle'):
		get_data(url, save=True)

	data = read_data()
	print(data.head())
