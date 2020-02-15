import sys

def main():
    file_name = sys.argv[1]
    try:
        with open(file_name) as fd:
            fd = fd.readlines()
        maxv = 0
        name = ""
        for line in fd:
            line = line.split()
            try:
                if int(line[0]) > maxv:
                    maxv = int(line[0])
                    name = " ".join(line[1:])
            except (ValueError):
                print("Invalid mark " + line[0] + " encountered. Skipping.")
        print("Best student: " + name)
        print("Best mark: " + str(maxv))
    except (FileNotFoundError):
        print("The file " + file_name + " could not be oppened.")

if __name__ == '__main__':
    main()
