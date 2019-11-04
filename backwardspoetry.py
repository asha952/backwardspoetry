# print("hello world")

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
    fragments.reverse()                        # split_poem is reversed
    print(fragments)
    iterator = length_of_list
    for lines in fragments:
        print("{} {}".format(length_of_list, lines))


lines_printed_backwards(split_poem, length_list)
