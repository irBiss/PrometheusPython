import sys


def find_most_frequent(string):
 words = {}
 strip = string.whitespace + string.punctuation + string.digits + "\"'"
 filename = 'file'
 for line in open(filename):
    for word in line.lower().split():
        word = word.strip(strip)
        if len(word) > 2:
            words[word] = words.get(word, 0) + 1
 for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))
 
	   
	   
print find_most_frequent('to understand recursion you need first to understand recursion...')