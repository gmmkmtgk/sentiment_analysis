# Sentiment Analysis using TextBlob and NLTK

This program performs sentiment analysis on a given text file using TextBlob and NLTK libraries. The sentiment is classified as positive, negative, or neutral, and an emotion is assigned based on the polarity score.

## Prerequisites

This program requires the following Python libraries to be installed:

- nltk
- textblob

It also requires the `vader_lexicon` resource from the NLTK library, which can be downloaded using the following command:

nltk.download('vader_lexicon')


## Usage

1. Place the text file to be analyzed in the same directory as the Python script and name it `textfile.txt`.
2. Run the Python script using the following command:

python sentiment_analysis.py


3. The program will print the sentiment analysis results, including the sentiment category, polarity score, and assigned emotion, as well as the sentiment percentages using NLTK's Vader sentiment analysis tool.

## Example

The following is an example of how the program can be used:

Sentiment analysis results:
Sentiment: Positive
Polarity: 0.55
Emotion: Happiness

Sentiment percentages:
Neg: 4.90%
Neu: 27.08%
Pos: 67.02%


This indicates that the sentiment of the text is positive, with a polarity score of 0.55 and an assigned emotion of happiness. The sentiment percentages using NLTK's Vader tool show that 67.02% of the text is classified as positive, 27.08% as neutral, and 4.90% as negative.
