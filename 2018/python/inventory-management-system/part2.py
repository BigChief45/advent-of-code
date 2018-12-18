"""
--- Day 2: Inventory Management System ---

https://adventofcode.com/2018/day/2
"""
from itertools import combinations


def main():
    with open('input.txt', 'r') as input_file:
        ids = input_file.read().splitlines()

    # Find the correct boxes
    correct_boxes = []
    for id1, id2 in combinations(ids, 2):
        diff = 0
        for c1, c2 in zip(id1, id2):
            if diff > 1:
                break

            if c1 != c2:
                diff += 1
        else:
            correct_boxes.append(id1)
            correct_boxes.append(id2)

    # Get the common letters in the correct boxes found.
    # We already know that there are 2 correct boxes
    letters = ''
    for c1, c2 in zip(correct_boxes[0], correct_boxes[-1]):
        if c1 == c2:
            letters += c1

    print(letters)


if __name__ == '__main__':
    main()
