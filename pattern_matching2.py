import sys

def main():
    f = open("C:\\Users\\mtoback\\Documents\\bioinformatics\\Vibrio_cholerae.txt")
    pattern = "CTTGATCAT"
    len_pattern = len(pattern)
    genome = f.read()
    len_genome = len(genome)
    matches = []
    for idx in range(0,len_genome-len_pattern+1):
        if genome[idx:idx+len_pattern] == pattern:
            matches.append(idx)
    for match in matches:
        print(match, end=" ")


if __name__ == "__main__":
    main()