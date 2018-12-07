import os
from AVLTree import AVLTree,Node
from RedBlackTree import RedBlackTree,RBTNode
###Searches for each anagrams in the list and returns a counter for each valid anagram

def count_anagrams(anagrams,english_words):
    counter = 0
    for item in anagrams:
        if english_words.search(item):
            counter += 1
    return counter

# creates 2 arrays used to search and compare the number of anagrams between a list of words
# returns the word with the most valid anagrams in the file
def most_anagrams(english_words):
    name_file = "random_words.txt"
    f = open(name_file)
    line = f.readline()
    words = []

    while line:  # reads line by line to not run out of memory; gets only the passwords

        try:  # ignores line if irregularity with data

            words.append(line.rstrip())
            # print(line.rstrip())
        except:
            print()
        line = f.readline()

    f.close()
    num_anagrams = [0]*len(words)
    for i in range(len(words)):
        num_anagrams[i] = count_anagrams(all_perms(words[i]),english_words)
    max_word= words[0]
    max_count = 0
    for i in range(len(num_anagrams)):
        if max_count < num_anagrams[i]:
            max_count = num_anagrams[i]
            max = words[i]
    return max_word
# returns an array of all the possible permutations of a word/string
def all_perms(elements):
    temp_word = ""
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

def RedBlackSolution(name_file):
    f = open(name_file)
    line = f.readline()
    english_words = RedBlackTree()
    while line:  # reads line by line to not run out of memory; gets only the passwords
        try:  # ignores line if irregularity with data
            english_words.insert(Node(line.rstrip()))
            print(line.rstrip())
        except:
            print()
        line = f.readline()

    f.close()

    return english_words
def AVLTreeSolution(name_file):
    f = open(name_file)
    line = f.readline()
    english_words = AVLTree()

    while line:  # reads line by line to not run out of memory; gets only the passwords

        try:  # ignores line if irregularity with data

            english_words.insert(Node(line.rstrip()))
            print(line.rstrip())
        except:
            print()
        line = f.readline()

    f.close()
    return english_words
def main():

    name_file = 'shorter_list.txt'
    tree_decider = 2

    while tree_decider != 1 and tree_decider != 0:
        tree_decider = int(input("Enter 0 for AVL Tree   Enter 1 for Red Black Tree"))

    word_test = input(" Enter the word you would like to test for english language anagrams")
    if tree_decider == 0:
        english_words = AVLTreeSolution(name_file)
    else:
        english_words = RedBlackSolution(name_file)
    anagrams = all_perms(word_test)
    print(count_anagrams(anagrams,english_words))
    print(most_anagrams(english_words))


main()