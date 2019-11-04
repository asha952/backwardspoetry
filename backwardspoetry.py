# print("hello world")
import random

poem = """I like potatoes
They are interesting
Also they are versatile
You can make fries
Or even mashed potatoes"""

backwardsPoem = """
5 Or even mashed potatoes
4 You can make fries
3 Also they are versatile
2 They are interesting
1 I like potatoes
"""
split_poem = poem.split('\n')
length_list = len(split_poem)


def lines_printed_backwards(fragments, length_of_list):
    iterator = length_of_list
    while iterator > 0:
        print("{} {}".format(iterator, fragments[iterator-1]))
        iterator -= 1


def lines_printed_random(fragments, length_of_list):
    iterator = length_of_list
    while iterator > 0:
        print(fragments[random.randint(0,3)])
        iterator -= 1


#lines_printed_backwards(split_poem, length_list)
lines_printed_random(split_poem,length_list)