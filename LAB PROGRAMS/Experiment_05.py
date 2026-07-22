from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "playing", "studies", "happily", "connected"]
for word in words:
    print(word, "->", ps.stem(word))


Output :
running -> run
playing -> play
studies -> studi
happily -> happili
connected -> connect
