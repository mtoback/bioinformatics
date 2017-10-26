'''
Created on Oct 22, 2017

@author: mtoback
'''
import math
import sys
def main(args):
    values_str = args[0]
    values = values_str.split(",")
    matrix = []
    for value in values:
        char_list = []
        for char in value:
            char_list.append(char)
        matrix.append(char_list)
    num_cols = len(matrix[0])
    num_rows = len(matrix)
    entropy = 0
    for col in range(num_cols):
        num_as = 0
        num_cs = 0
        num_gs = 0
        num_ts = 0
        for row in range(num_rows):
            char =  matrix[row][col]
            if char == 'A':
                num_as += 1
            elif char == 'C':
                num_cs += 1
            elif char == 'G':
                num_gs += 1
            elif char == 'T':
                num_ts += 1
            else:
                print("invalid character: %s" % char)
                sys.exit(-1)
        if num_as > 0:
            entropy -= (num_as/num_cols)* math.log2(num_as/num_cols)
        if num_cs > 0:
            entropy -= (num_cs/num_cols)* math.log2(num_cs/num_cols)
        if num_gs > 0:
            entropy -= (num_gs/num_cols)* math.log2(num_gs/num_cols)
        if num_ts > 0:
            entropy -= (num_ts/num_cols)* math.log2(num_ts/num_cols)
    print(entropy)
if __name__ == '__main__':
    main(sys.argv[1:])