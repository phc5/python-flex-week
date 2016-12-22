import pandas as pd
import statistics
import vincent
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from pandas.tseries.resample import TimeGrouper
from pandas.tseries.offsets import DateOffset
from textblob import TextBlob

"""
	Converted MongoDB data into a CSV file. Then create a pandas dataframe from the CSV file
	and makes the created_at the index and changes the timezone to US/Pacific.

	lakers1m will be the count of tweets per minute
	lakers1m.head()
	lakers1m.describe(include='all')
	lakers1m.mean()
	Mongo -> CSV: mongo to csv: mongoexport --host localhost --db dbname --collection name --csv --out text.csv --fields field1, field2, field3
"""
lakers = pd.read_csv('/Users/paulchong/Desktop/Thinkful/Python/twitterAnalysis/lakers.csv')
lakers['created_at'] = pd.to_datetime(pd.Series(lakers['created_at']))
lakers.set_index('created_at', drop=False, ilakerslace=True)
lakers.index = lakers.index.tz_localize('GMT').tz_convert('US/Pacific')
lakers1m = lakers['created_at'].resample('1t').count()


# # Use this in jupyter to get a graph of tweets per minute
# vincent.core.initialize_notebook()
# area = vincent.Area(lakers1m)
# area.colors(brew='Spectral')
# area.display()
# # # # # # # # # # # # # # # # # # #

"""
	Tokenize the tweets and filter out all stop words (which are high frequency words 
	that are common and irrelevant). Print out top fifteen sources and plot them on 
	a line graph.
"""
# stop = stopwords.words('english')
# text = np['text']
# tokens = []
# for txt in text.values:
# 	tokens.extend([t.lower().strip(":,.") for t in txt.split()])

# 	filtered_tokens = [w for w in tokens if not w in stop]
# 	freq_distribution = nltk.FreqDist(filtered_tokens)
# print(freq_distribution.most_common(25))
# freq_distribution.plot(25)

# count = 0
# while count < 15:
# 	print('{} {}'.format(np.source[count], np.source.value_counts()[count]))
# 	count += 1

# source = nltk.FreqDist(np.source)
# source.plot(15)

"""
	Create a list of all text from the tweets. For each tweet, make them into a Textblob
	object and perform sentiment analysis on it appending polarity and subjectvitiy to their
	respective lists. 
	Polarity measures how positive or negative the tweet is [-1.0, 1.0].
	Subjectivity measures how much of an opinion or fact the tweet is [0.0, 1.0]
"""
text = lakers['text']
polarity = []
subjectivity = []
for tweet in text.values:
	print(tweet)
	analysis = TextBlob(tweet)
	print(analysis.sentiment, '\n')
	polarity.append(analysis.sentiment.polarity)
	subjectivity.append(analysis.sentiment.subjectivity)
print('Polarity: \n Mean: {} \n Median: {} \n Mode: {} \n Max: {} \n Min: {}'.format(statistics.mean(polarity), statistics.median(polarity), statistics.mode(polarity), max(polarity), min(polarity)))
print('Subjectivity: \n Mean: {} \n Median: {} \n Mode: {} \n Max: {} \n Min: {}'.format(statistics.mean(subjectivity), statistics.median(subjectivity), statistics.mode(subjectivity), max(subjectivity), min(subjectivity)))


