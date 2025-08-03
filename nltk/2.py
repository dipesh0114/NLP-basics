import nltk

text = """Welcome you to programming Knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demoWords = ["playing","happiness","going","doing","yes","no","I","having","had","haved"]

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
# print(stop_words)

from nltk.tokenize import word_tokenize,sent_tokenize

tokenize_words = word_tokenize(text)
# print(tokenize_words)

without_stop_words = []
for word in tokenize_words:
    if word not in stop_words:
        without_stop_words.append(word)

print(without_stop_words)        