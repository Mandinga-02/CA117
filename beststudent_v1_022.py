import sys

def main():
    try:
        file = sys.argv[1]
        f = open(file, 'r')

        highest = 0
        for lines in f:
            lines = lines.strip().split()
            # print(lines)
            mark = int(lines[0])
            name = ' '.join(lines[1:])
            if mark > highest:
                highest = mark
            highest = highest
        print('Best student: {:s}'.format(name))
        print('Best mark: {:}'.format(highest))
    except FileNotFoundError:
        print('The file {:s} could not be opened'.format(file))

if __name__ == '__main__':
    main()
