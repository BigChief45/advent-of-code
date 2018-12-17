"""
--- Day 2: Inventory Management System ---

https://adventofcode.com/2018/day/2
"""
from collections import Counter


def main():
    two_letters_count, three_letters_count = 0, 0

    with open('input.txt', 'r') as input_file:
        for i in input_file:
            counter = Counter(i)
            counts = counter.values()

            if 2 in counts:
                two_letters_count += 1

            if 3 in counts:
                three_letters_count += 1

    checksum = two_letters_count * three_letters_count
    print(checksum)


if __name__ == '__main__':
    main()
