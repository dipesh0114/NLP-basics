import nltk

text = """Welcome you to programming Knowledge. Lets start with our first tutorial on NLTK. We shall learn the basics of NLTK here."""
demoWords = ["playing","happiness","going","doing","yes","no","I","having","had","haved", "coding", "programming"]

from nltk.stem import PorterStemmer, WordNetLemmatizer

lemmatizer = WordNetLemmatizer()  # acts as a constructor object to their classes 
stemmer = PorterStemmer()

for word in demoWords:
    print(word, stemmer.stem(word), lemmatizer.lemmatize(word,"v"))


from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()  #to initialize the class
score = sia.polarity_scores("Programming is fun")

print(score)  #{'neg': 0.0, 'neu': 0.377, 'pos': 0.623, 'compound': 0.5106} this indicates it is a positive statement

print(sia.polarity_scores("you are very bad and you should get lost"))
