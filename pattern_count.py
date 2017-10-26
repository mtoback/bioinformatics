import sys
def main(argv):
    count = 0
    dataset = argv[0]
    pattern = argv[1]
    ld = len(dataset)
    lp = len(pattern)
    for idx in range(0,ld-lp+1):
        if dataset[idx:idx+lp] == pattern:
            count = count + 1
    print(count)
    
if __name__ == "__main__":
    main(sys.argv[1:])
    