"""
--- Day 1: Chronal Calibration ---

https://adventofcode.com/2018/day/1
"""
from functools import reduce


def main():
    with open('input.txt', 'r') as input_file:
        frequencies = map(lambda l: int(l), input_file.readlines())

    frequency = reduce(lambda j,k: j + k, frequencies)
    print(frequency)


if __name__ == '__main__':
    main()
