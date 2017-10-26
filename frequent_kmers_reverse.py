'''
Created on Oct 14, 2017

@author: mtoback
'''
import sys
class FrequentKmersReverse(object):
    def __init__(self):
        self.nucleotide = ['A', 'C', 'G', 'T']

    def neighbors(self, pattern, d):
        if d == 0:
            return [pattern]
        if len(pattern) == 1:
            return set(self.nucleotide)
        neighborhood = set()
        suffix_neighbors = self.neighbors(pattern[:-1], d)
        for suffix_neighbor in suffix_neighbors:
            if self.hamming(pattern[:-1], suffix_neighbor) < d:
                for nucleotide in self.nucleotide:
                    neighborhood.add(nucleotide+suffix_neighbor)
            else:
                neighborhood.add(pattern[0] + suffix_neighbor)
        return neighborhood
                
    def reverse(self, pattern):
        output = []
        for ch in pattern:
            if ch == 'A':
                output.append('T')
            elif ch == 'T':
                output.append('A')
            elif ch == 'C':
                output.append('G')
            else:
                output.append('C')
        output_str = ''.join(output)[::-1]
        return output_str
    
    def hamming(self, first, second):
        distance = 0
        for idx in range(len(first)):
            if first[idx] != second[idx]:
                distance += 1
        return distance

    def get_frequent_words(self, genome, k_len, max_hamming):
        values = ['A','C','G','T']
        max_count = 0
        matches = {}
        for i in range(4**k_len):
            val = i
            vals = []
            for idx in range(k_len):
                vals.append(values[0])
            pos = 0
            while val >= 4:
                vals[k_len - 1 - pos] = values[val % 4]
                val = int(val/4)
                pos = pos + 1
            vals[k_len - 1 - pos] = values[val]
            pattern = ''.join(vals)
            for idx in range(len(genome)-k_len-1):
                if self.hamming(pattern, genome[idx:idx+k_len]) <= max_hamming:
                    if pattern in matches:
                        matches[pattern] += 1
                    else:
                        matches[pattern] = 1
                    if matches[pattern] > max_count:
                        max_count = matches[pattern]
                reverse_comp = self.reverse(pattern)
                if self.hamming(reverse_comp, genome[idx:idx+k_len]) <= max_hamming:
                    if pattern in matches:
                        matches[pattern] += 1
                    else:
                        matches[pattern] = 1
                    if matches[pattern] > max_count:
                        max_count = matches[pattern]
        frequent_words = []
        for key,value in matches.items():
            if value == max_count:
                frequent_words.append(key)
        return frequent_words

def main(args):
    genome = None 
    max_hamming = None 
    k_len = None
    if len(args) == 1:
        f = open(args[0])
        genome =  f.readline().strip()
        k_len = int(f.readline())
        max_hamming = int(f.readline().strip())
    else:
        genome = args[0] 
        k_len = int(args[1])
        max_hamming = int(args[2])
    fk = FrequentKmersReverse()
    print(fk.get_frequent_words(genome, k_len, max_hamming))

if __name__ == "__main__":
    main(sys.argv[1:])