print("hello world")

poem = """ I like potatoes
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

def lines_printed_backwards(fragments):
    for lines in reversed(split_poem):

    print()
