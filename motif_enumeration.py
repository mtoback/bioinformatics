'''
Created on Oct 19, 2017

@author: mtoback
'''
import sys
from neighbors import FrequentKmers
from approximate_match import ApproximateMatch
import neighbors
class MotifEnumeration(object):
    '''
    classdocs
    '''
    def __init__(self, genomes, k, d):
        '''
        Constructor
        '''
        self.genomes = genomes
        self.kmer_size = k
        self.max_hamming = d
        self.neighbors = FrequentKmers()
        self.approximate_match = ApproximateMatch()
    def solve(self):
        patterns = set()
        genome_num = -1
        for genome in self.genomes:
            genome_num += 1
            len_genome = len(genome)
            for idx in range(len_genome - self.kmer_size+1):
                if idx==15 and genome_num == 1:
                    pass
                kmer_patterns = self.neighbors.neighbors(genome[idx:idx+self.kmer_size], self.max_hamming)
                for kmer_pattern in kmer_patterns:
                    add_pattern = True
                    for all_genome in self.genomes:
                        if self.approximate_match.has_match(kmer_pattern, all_genome, self.max_hamming):
                            continue
                        else:
                            add_pattern = False
                            print("pattern %s did not match genome %s" % (kmer_pattern, all_genome))
                            break
                    if add_pattern:
                        patterns.add(kmer_pattern)
        return patterns

def main(args):
    k = int(args[0])
    d = int(args[1])
    genomes = args[2:]
    me = MotifEnumeration(genomes, k, d)
    result = me.solve()
    print(' '.join(sorted(result)))
if __name__ == "__main__":
   main(sys.argv[1:])
            
        
        