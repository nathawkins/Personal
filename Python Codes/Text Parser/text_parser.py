'''
Allows the user to parse through a text file. Where something like control-F
will show you results for where something appears in a document, this will show
any mention of a specific word in context. After loading in a given text file,
this will look for any mention of word(s) and give the associated context in
which they were used.

Author: Nat Hawkins
Date: 25 April, 2017
'''

#Opens the text file and reads in the line of text.
text = open('test.txt', "r").read()

#This will strip away any kind of unnnecessary punctuation in sentencing.
#If there is any additional punctuation or symbols you wish to ignore, they can
#be added in the form of text = text.replace("what you want ignored","").
text = text.replace(",", "")
text = text.replace("?", ".")
text = text.replace("!", ".")
text = text.replace("[","")
text = text.replace("]","")
text = text.replace("(","")
text = text.replace(")","")
text = text.replace("{","")
text = text.replace("}","")

#Creates an array of the document. Splits based on location of the periods.
#Appended above with text replacing commands.
split = text.split('.')

#Defines the process of actually searching for the word and pulling out
#associated sentences.
def search_words(word, sentences):
    for i in sentences:
        cleaned = i.lower()
        words = cleaned.split()
        if word in words:
            print(i,".")

#Put the words in the array in the form of 'strings' and search away!
list_of_words =[] #use lower case for words
for something in list_of_words:
    search_words(something,split)
