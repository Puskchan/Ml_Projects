from textblob import TextBlob
from newspaper import Article
# import nltk
#
# nltk.download('punkt')

""" This part is just for news analysis"""
# # neutral
# url = 'https://en.wikipedia.org/wiki/Mathematics'
#
# # happy
# url_1 = 'https://www.newindianexpress.com/world/2022/nov/22/indian-wildlife-biologist-honoured-with-uns-highest-environmental-award-2520993.html'
#
# # sad
# url_2 = 'https://www.thehindu.com/news/cities/Delhi/mehrauli-murder-aftab-will-kill-me-cut-me-into-pieces-shraddha-told-maharashtra-police-in-2020/article66173056.ece'
#
# article = Article(url_2)
#
# article.download()
# article.parse()
# article.nlp()
#
# text = article.summary
# print(text)

""" This part is there if you want to analyze your own text"""
with open('mytext.txt','r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
