'''
Created on Oct 14, 2017

@author: mtoback
'''
import sys
def main(args):
    first = args[0]
    second = args[1]
    distance = 0
    for idx in range(len(first)):
        if first[idx] != second[idx]:
            distance += 1
    print(distance)
    
if __name__ == '__main__':
    main(sys.argv[1:])