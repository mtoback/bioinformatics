import sys

def main(argv):
    pattern = argv[0]
    len_pattern = len(pattern)
    genome = argv[1]
    len_genome = len(genome)
    matches = []
    for idx in range(0,len_genome-len_pattern+1):
        if genome[idx:idx+len_pattern] == pattern:
            matches.append(idx)
    for match in matches:
        print(match, end=" ")


if __name__ == "__main__":
    main(sys.argv[1:])