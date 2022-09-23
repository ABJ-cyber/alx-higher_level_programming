#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        print(f"{1:d} argument:")
        print(f"{1:d}: {sys.argv[1]}")
    elif len(sys.argv) == 1:
        print(f"{0:d} arguments.")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print(f"{i:d}: {sys.argv[i]}")
