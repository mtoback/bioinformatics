'''
Created on Oct 22, 2017

@author: mtoback
'''
from math import inf
import sys

from neighbors import FrequentKmers

class MedianString(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.hamming = FrequentKmers()
        self.nucleotide = ['A', 'C', 'G', 'T']
        self.k = int(params[0])
        self.dna = params[1:]

    def numToString(self,n,k):
        str = ""
        while n > 3:
            val = n % 4
            str = self.nucleotide[val] + str
            n = int(n/4)
        str = self.nucleotide[n] + str
        if len(str) < k:
            for idx in range(k-len(str)):
                str = "A" + str
        return str


    def findMedianString(self):
        count = 4**self.k
        distance = [self.numToString(0, self.k), 999999]
        
        for num in range(count):
            kmer = self.numToString(num, self.k)
            ham_distance = distance[1]
            distances = []
            for genome in self.dna:
                if kmer in genome:
                    distances.append(0)
                    continue
                genome_distance = ham_distance                
                len_genome = len(genome)
                for idx in range(len_genome - self.k+1):
                    hamming_d = self.hamming.hamming(genome[idx:idx+self.k], kmer)
                    if hamming_d < genome_distance:
                        genome_distance = hamming_d
                distances.append(genome_distance)
            kmer_distance = sum(distances)
            if kmer_distance < distance[1]:
                distance = [kmer, kmer_distance]
        return distance[0]

def main(args):
    ms = MedianString(args)
    print(ms.findMedianString())
if __name__ == "__main__":
    main(sys.argv[1:])