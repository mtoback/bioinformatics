'''
Created on Oct 24, 2017

@author: mtoback
'''
import sys
class Profile(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def calculate_profile(self, dna):
        motif = []
        num_rows = len(dna)
        for row in dna:
            row_chars = []
            for char in row:
                row_chars.append(char)
            motif.append(row_chars)
        num_cols = len(motif[0])
        profile = [[0.0 for _x in range(num_cols)] for _y in range(4)]
        for col in range(num_cols):
            num_as = 0
            num_cs = 0
            num_gs = 0
            num_ts = 0
            for row in range(num_rows):
                char =  motif[row][col]
                if char == 'A':
                    num_as += 1
                elif char == 'C':
                    num_cs += 1
                elif char == 'G':
                    num_gs += 1
                elif char == 'T':
                    num_ts += 1
             
            profile[0][col] = num_as/num_rows
            profile[1][col] = num_cs/num_rows
            profile[2][col] = num_gs/num_rows
            profile[3][col] = num_ts/num_rows
        return profile

def main(args):
    motif = args[:]
    profile = Profile()
    print(profile.calculate_profile(motif))

if __name__ == "__main__":
    main(sys.argv[1:])