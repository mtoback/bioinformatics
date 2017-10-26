'''
Created on Oct 23, 2017

@author: mtoback
'''
import sys

class MostProbableKmer(object):
    '''
    classdocs
    '''


    def __init__(self, genome, k, probabilities):
        '''
        Constructor
        '''
        self.genome = genome
        self.k = k
        self.p_matrix = [[0 for _x in range(self.k)] for _y in range(4)]
        row = 0
        col = 0
        for row_prob in probabilities:
            for col_prob in row_prob:
                self.p_matrix[row][col] = float(col_prob)
                if col == k-1:
                    col = 0
                    row = row + 1
                else:
                    col = col + 1
        self.nucleotides = ['A','C','G','T']
        
    def find_prob(self, kmer):
        probability = 1.0
        for idx in range(self.k):
            probability *= self.p_matrix[self.nucleotides.index(kmer[idx])][idx]
        return probability

    def find_kmer(self):
        prob = -1.0
        position = -1
        for idx in range(len(self.genome) - self.k):
            next_prob = self.find_prob(self.genome[idx:idx+self.k]) 
            if next_prob > prob:
                prob = next_prob
                position = idx
        return self.genome[position:position+self.k]
        
def main(args):
    genome = args[0]
    k = int(args[1])
    probabilities = args[2:]
    profile = MostProbableKmer(genome, k, probabilities)
    print(profile.find_kmer())

if __name__ == "__main__":
    main(sys.argv[1:])