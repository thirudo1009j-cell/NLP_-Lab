import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
word = input("Enter a word : ")
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print("Original : ", word)
print("Stem : ", stemmer.stem(word))
print("Lemma : ", lemmatizer.lemmatize(word, pos="v"))



Output :
Enter a word : running
Original :  running
Stem :  run
Lemma :  run
