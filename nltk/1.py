import nltk
import matplotlib.pyplot as plt

# nltk.download()   # to download specific or all packages from NLTK library

text = """Welcome you to programming Knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""

from nltk.tokenize import word_tokenize
word_tokenized = word_tokenize(text)
# print(word_tokenized)    #word tokenization

# from nltk.tokenize import sent_tokenize
# print(sent_tokenize(text))     #sentence tokenization

from nltk.probability import FreqDist
fd = FreqDist(word_tokenized)
print(fd)
print(fd.most_common(3))
fd.plot(30, cumulative=False)
plt.show()