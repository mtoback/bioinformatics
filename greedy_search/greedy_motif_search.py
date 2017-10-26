'''
Created on Oct 23, 2017

@author: mtoback
'''
import sys
from greedy_search.most_probable_kmer import MostProbableKmer
from greedy_search.profile import Profile
from greedy_search.score import Score
class GreedyMotifSearch(object):
    '''
    classdocs
    '''


    def __init__(self, k, t, dna):
        '''
        Constructor
        '''
        self.k = k
        self.t = t
        self.dna = dna
        self.motif = []
        self.profile = Profile()
        self.best_motifs = []
        for row in self.dna:
            self.best_motifs.append(row[0:self.k])
        self.score = Score()
        self.best_score = self.score.find_score(self.best_motifs)
        
    
    def find_motif(self):
        for idx in range(len(self.dna[0])-self.k):
            motif = [self.dna[0][idx:idx+self.k]]
            probabilities = self.profile.calculate_profile(motif)
            for row in self.dna[1:]:
                mpk = MostProbableKmer(row, self.k, probabilities)
                kmer = mpk.find_kmer()
                motif.append(kmer)
                probabilities = self.profile.calculate_profile(motif)
            score = self.score.find_score(motif)
            if score < self.best_score:
                self.best_score = score
                self.best_motifs = motif
        return self.best_motifs
def main(args):
    k = int(args[0])
    t = int(args[1])
    dna = args[2:]
    gms = GreedyMotifSearch(k, t, dna)
    results = gms.find_motif()
    for result in results:
        print(result)
if __name__ == "__main__":
    main(sys.argv[1:])
        