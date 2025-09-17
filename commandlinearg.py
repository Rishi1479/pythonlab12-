import sys
def main():
    print("Number of arguments:", len(sys.argv)-1)
    for i in range(1,len(sys.argv)):
        print("Arguments:", sys.argv[i])
    if len(sys.argv) > 1:
        print("First argument:", sys.argv[1])
    else:
        print("No arguments were passed (except the script name).")
if __name__ == "__main__":
    main()