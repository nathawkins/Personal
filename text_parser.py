text = open('''file you want to look through. txt''', "r").read()

split = text.split('.')
#print(split)

def search_words(word, sentences):
    for i in sentences:
        cleaned = i.lower()
        words = cleaned.split()
        if word in words:
            print(i,".")

list_of_words =['''put words you want to find here''']
for something in list_of_words:
    search_words(something,split)
