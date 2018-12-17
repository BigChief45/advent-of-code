"""
--- Day 1: Chronal Calibration ---

https://adventofcode.com/2018/day/1
"""
def main():
    with open('input.txt', 'r') as input_file:
        frequencies = list(map(lambda l: int(l), input_file.readlines()))

    changes = []
    current = 0
    duplicate_found = False
    while not duplicate_found:
        for frequency in frequencies:
            current += frequency
            
            if current in changes:
                print('First frequency reached twice:', current)
                duplicate_found = True
                return

            changes.append(current)


if __name__ == '__main__':
    main()
