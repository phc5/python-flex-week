# Analyzing Twitter with Python

## Use
Clone repository.
cd into project directory and make sure to install all modules used in this project.
#### For Streaming
Edit twitter.py
- change database name -> self.db = pymongo.MongoClient().'db name'
- change filter 'sapi.filter(track=[words to filter separated by commas'])
In project directory, python3 twitter.py.
Export mongodb data into CSV file.
- mongo to csv: mongoexport --host localhost --db dbname --collection name --csv --out text.csv --fields field1, field2, etc..
#### For Analysis and Visualization
Edit sentiment.py
- change pd.read_csv to point to you CSV file.
For tweets per minute plot:
- jupyter notebook in terminal
- copy and paste lines 21 - 31 along with modules into the notebook and run.
For word frequency and source plot:
- open jupyter notebook:
- copy and paste lines 21 - 25 and 39- 51 along with modules.
For sentiment analysis:
- comment out lines 27 - 51
- python3 sentiment.py

## Important Modules used:
[Tweepy](http://www.tweepy.org/ "Tweepy")
- An easy-to-use Python library for accessing Twitter API.
- Used to have access to Twitter's data.

[PyMongo](https://api.mongodb.com/python/current/ "PyMongo")
- A Python distro containing tools for working with MongoDB.
- Used to store streamed tweets.

[pandas](http://pandas.pydata.org/ "pandas")
- An open-source, BSD-licensed library that provides high-performance, easy-to-use data structures and analysis tools.
- Used to make data easily accessible and usable.

[Vincent](https://vincent.readthedocs.io/en/latest/ "Vincent")
- Python to Vega (visualization grammar) translator. The data capabilities of Python with the visualization capabilities of JavaScript.
- Used to visualize tweets per minute data.

[NLTK](http://www.nltk.org/ "Natrual Langauage Toolkit")
- NLTK is a platform for building Python programs to work with human language data. 
- Used for finding frequency of words in tweets.

[TextBlob](https://textblob.readthedocs.io/en/dev/ "TextBlob")
- A Python library for processing textual data.
- Used for sentiment analysis.
	
