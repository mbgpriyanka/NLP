from nltk.book import *

#☼ 3.The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?

print(['Monty', 'Python'] * 20)
#☼ Review 1 on computing with language. How many words are there in text2? How many distinct words are there?
print('Number of words in text2 :',len(text2))
print('Number of distinct words in text2 :',len(set(text2)))

#☼ 5 -Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
#print()
#print('Lexically diverse is :-',)

#6-Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby.
# #What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?
#print(text2.dispersion_plot(["Elinor", "Marianne", "Edward","Willoughby"]))

# 7-  Find the collocations in text5.
print('collocations in text5',text5.collocations())


#8 -☼ Consider the following Python expression: len(set(text4)). State the purpose of this expression.
# Describe the two steps involved in performing this computation.

print('Distinct words in text4:',len(set(text4)))

#9  Review 2 on lists and strings.
#Define a string and assign it to a variable, e.g., my_string = 'My String' (but put something more interesting in the string).
# Print the contents of this variable in two ways, first by simply typing the variable name and pressing enter, then by using the print statement.
#Try adding the string to itself using my_string + my_string, or multiplying it by a number, e.g., my_string * 3. Notice that the strings are joined together without any spaces. How could you fix this?
mystring ='Good morning'
mystring
print('9-a',mystring)
print('9-b',mystring+mystring)
print('9-c',mystring*3)
print('9-d',mystring+' ' + mystring)

#10 -Define a variable my_sent to be a list of words, using the syntax my_sent = ["My", "sent"] (but with your own words, or a favorite saying).
#Use ' '.join(my_sent) to convert this into a string.
#Use split() to split the string back into the list form you had to start with.
my_sent = ["Happy", "New ","Year"]
print('10 a -',' '.join(my_sent))
print('10 b -',' '.join(my_sent).split())

#11 Define several variables containing lists of words, e.g., phrase1, phrase2, and so on. Join them together in various combinations (using the plus operator) to form whole sentences.
# What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?
phrase1 =sent1
phrase2 = sent3
print('11-a',len(phrase1+phrase2))
print('11-b',len(phrase1)+len(phrase2))

# 12 Consider the following two expressions, which have the same value. Which one will typically be more relevant in NLP? Why?
#
# "Monty Python"[6:12]
# ["Monty", "Python"][1]
print('12-a:',"Monty Python"[6:12])
print('12-b:',["Monty", "Python"][1])

#13 - We have seen how to represent a sentence as a list of words, where each word is a sequence of characters. What does sent1[2][2] do? Why?
# Experiment with other index values.
print('13-a',sent1[2][2])

#14 The first sentence of text3 is provided to you in the variable sent3. The index of the in sent3 is 1, because sent3[1] gives us 'the'.
# What are the indexes of the two other occurrences of this word in sent3?
#print(sent3)
print('14: Indices are -',[index for index, value in enumerate(sent3) if value == 'the'])


#15 Review the discussion of conditionals in 4. Find all words in the Chat Corpus (text5) starting with the letter b.
# Show them in alphabetical order.
print('15-',sorted([w for w in text5 if w.startswith('b')]))

#16 Type the expression list(range(10)) at the interpreter prompt.
# Now try list(range(10, 20)), list(range(10, 20, 2)), and list(range(20, 10, -2)).
# We will see a variety of uses for this built-in function in later chapters.

print('16-a:',list(range(10)))
print('16-b:',list(range(10, 20)))
print('16-c:',list(range(10, 20, 2)))
print('16-d:',list(range(10, 20, -2)))

#17 Use text9.index() to find the index of the word sunset.
# You'll need to insert this word as an argument between the parentheses.
# By a process of trial and error, find the slice for the complete sentence that contains this word

print('17-a',text9.index('sunset'))
print('17-b',text9[620:630])

#18 Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.
print()
totalsent =[]
for k in ["sent"+str(i) for i in range(1,10)]:
    totalsent += eval(k)
#print('18 -',sorted(totalsent))
print('18 -',len(totalsent))

#19 What is the difference between the following two lines? Which one will give a larger value?
# Will this be the case for other texts?
print('19-a',len(sorted(set(w.lower() for w in text1))))
print('19-b',len(sorted(w.lower() for w in set(text1))))


#20 What is the difference between the following two tests: w.isupper() and not w.islower()?
w = 'GOOD MORNING'
print('20-a',w.isupper())
print('20-b',not w.islower())

#21 Write the slice expression that extracts the last two words of text2.
print('21-',text2[-2:])


#22 Find all the four-letter words in the Chat Corpus (text5).
# With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.
fd = FreqDist(text5)
flwords = sorted(set([w for w in text5 if w.isalpha() and len(w) == 4]))
print('22-',len(flwords)) ####have to do

#23 Review the discussion of looping with conditions in 4.
# Use a combination of for and if statements to loop over the words of the movie script
# for Monty Python and the Holy Grail (text6) and print all the uppercase words, one per line.
print('23 -',[w for w in text6 if w.upper()])

#24 Write expressions for finding all words in text6 that meet the conditions listed below.
# The result should be in the form of a list of words: ['word1', 'word2', ...].
#Ending in ise
print('24-a',[w for w in text6 if w.endswith('ise')])
#Containing the letter z
print('24-b',[w for w in text6 if 'z' in w])
#Containing the sequence of letters pt
print('24-c',[w for w in text6 if 'pt' in w])
#Having all lowercase letters except for an initial capital (i.e., titlecase)
print('24-d',[w for w in text6 if w.istitle()])

#25 Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'].
# Now write code to perform the following tasks:
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
#Print all words beginning with sh
print('25-a',[w for w in sent if w.startswith('sh')])
#Print all words longer than four characters
print('25-b',[w for w in sent if len(w)> 4])

#26 What does the following Python code do? sum(len(w) for w in text1)
# Can you use it to work out the average word length of a text?
print('26-a',sum(len(w) for w in text1))
print('26-b: Average',sum(len(w) for w in text1)/len(text1))

#27 Define a function called vocab_size(text) that has a single parameter for the text,
# and which returns the vocabulary size of the text.
def vocab_size(text):
    return len(set(text))
print('27 :Vocab size-',vocab_size(text2))

#28 Define a function percent(word, text) that calculates
# how often a given word occurs in a text, and expresses the result as a percentage.
def percent(word, text):
    fd = FreqDist(text)
    return float(fd[word]/len(text))*100
print('28-',percent('They',text2))

#29 We have been using sets to store vocabularies. Try the following Python expression: set(sent3) < set(text1).
# Experiment with this using different arguments to set().
# What does it do? Can you think of a practical application for this?
print('29-',set(sent3) < set(text1))











