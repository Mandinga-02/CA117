import sys

def student(f):

    names = ""
    highest = 0
    for s in f:
        try:
           details = s.split()
           mark = int(details[0])
           name = " ".join(details[1:])
           if mark > highest:
                highest = mark
                names = name
           elif mark == highest:
               names = names + ", " + name

        except(ValueError):
            print ("Invalid mark {:s} encountered. Skipping.".format(details[0]))

    print("Best student(s): {}".format(names))
    print("Best mark: {}".format(highest))

def main():
    try:
        students = sys.argv[1]
        f = open(students, "r")
        student(f)
        f.close()

    except(FileNotFoundError):
        print("The file {:s} could not be opened".format(students))

if __name__ == "__main__":
    main()
