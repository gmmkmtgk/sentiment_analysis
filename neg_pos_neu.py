import nltk
from textblob import TextBlob

# read the text file
with open('textfile.txt', 'r') as file:
    text = file.read()

# perform sentiment analysis using TextBlob
blob = TextBlob(text)
polarity = blob.sentiment.polarity

# determine the sentiment category based on polarity
if polarity < 0:
    sentiment = 'Negative'
elif polarity > 0:
    sentiment = 'Positive'
else:
    sentiment = 'Neutral'

# print the sentiment details and percentage
print('Sentiment analysis results:')
print('Sentiment: {}'.format(sentiment))
print('Polarity: {:.2f}'.format(polarity))

# perform sentiment analysis using NLTK
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)

# print the sentiment percentages
print('\nSentiment percentages:')
for category, score in scores.items():
    if category != 'compound':
        percent = score * 100
        print('{}: {:.2f}%'.format(category.capitalize(), percent))
