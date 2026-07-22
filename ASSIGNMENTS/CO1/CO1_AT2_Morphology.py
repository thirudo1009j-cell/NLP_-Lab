import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
words = ["playing", "connected", "studies", "running"]
print("Word\t\tStem\t\tLemma")
print("-" * 40)
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos='v')
    print(f"{word:12}{stem:12}{lemma}")


Output : 
 Word		     Stem		     Lemma
----------------------------------------
playing      play        play
connected   connect     connect
studies      studi       study
running      run         run
