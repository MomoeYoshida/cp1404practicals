"""
Write a program to count the occurrences of words in a string. The program should
ask the user for a string, then print the counts of how many of each word are in
the file. Use a dictionary where the keys are the words and the values are the
counts.
Sort the words.
Align the outputs so the numbers are in one nice column. You will need to find
the longest word in the list first.
"""
word_to_count = {}
text_str = input("Text: ")

words = text_str.split()
for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

words = list(word_to_count.keys())
words.sort()
longest_word = max((len(word)) for word in words)
for word in words:
    print("{:{}} : {}".format(word, longest_word, word_to_count[word]))
