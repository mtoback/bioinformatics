'''
Created on Oct 14, 2017

@author: mtoback
'''
import sys
class ApproximateMatch(object):
    def hamming(self, first, second):
        distance = 0
        for idx in range(len(first)):
            if first[idx] != second[idx]:
                distance += 1
        return distance

    def find_matches(self, pattern, genome,  max_hamming):
        matches = []
        len_pattern = len(pattern)
        for idx in range(len(genome)-len_pattern+1):
            if self.hamming(pattern, genome[idx:idx+len_pattern]) <= max_hamming:
                matches.append(str(idx))
        return matches
    
    def has_match(self, pattern, genome,  max_hamming):
        len_pattern = len(pattern)
        for idx in range(len(genome)-len_pattern+1):
            if self.hamming(pattern, genome[idx:idx+len_pattern]) <= max_hamming:
                return True
        return False

def main(args):
    pattern = args[0]
    genome = args[1]
    max_hamming = int(args[2])
    am = ApproximateMatch()
    matches = am.find_matches(pattern, genome,  max_hamming)
    count = 0
    for match in matches:
        sys.stdout.write("%s "% match)
        sys.stdout.flush()
        count += 1
        if count >= 20:
            count = 0
            print(" ")
    print(" ")
if __name__ == '__main__':
    main(sys.argv[1:])