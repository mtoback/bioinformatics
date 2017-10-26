'''
Created on Oct 14, 2017

@author: mtoback
'''
import sys
def hamming(first, second):
    distance = 0
    for idx in range(len(first)):
        if first[idx] != second[idx]:
            distance += 1
    return distance

def main(args):
    f = open("dataset_9_4.txt")
    pattern = args[0] # f.readline().strip()
    len_pattern = len(pattern)
    genome = args[1] # f.readline().strip()
    len_genome = len(genome)
    max_hamming = int(args[2]) # int(f.readline().strip())
    matches = []
    for idx in range(len_genome-len_pattern+1):
        if hamming(pattern, genome[idx:idx+len_pattern]) <= max_hamming:
            matches.append(str(idx))
    print(len(matches))
if __name__ == '__main__':
    main(sys.argv[1:])