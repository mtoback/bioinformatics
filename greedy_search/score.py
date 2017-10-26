'''
Created on Oct 24, 2017

@author: mtoback
'''
import sys
class Score(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def find_score(self,genomes):
        num_cols = len(genomes[0])
        num_rows = len(genomes)
        score = 0
        for col in range(num_cols):
            num_as = 0
            num_cs = 0
            num_gs = 0
            num_ts = 0
            for row in range(num_rows):
                char =  genomes[row][col]
                if char == 'A':
                    num_as += 1
                elif char == 'C':
                    num_cs += 1
                elif char == 'G':
                    num_gs += 1
                elif char == 'T':
                    num_ts += 1
            score += num_rows -  max(num_as, num_cs, num_gs, num_ts)
        return score
        
def main(args):
    genomes = args[:]
    score = Score()
    print(str(score.find_score(genomes)))

if __name__ == "__main__":
    main(sys.argv[1:])