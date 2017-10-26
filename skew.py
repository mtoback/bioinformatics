'''
Created on Oct 14, 2017

@author: mtoback
'''
import sys

def main(args):
    string = args[0]
    skew = ['0']
    val = 0
    for ch in string:
        if ch == 'C':
            val -=1;
        elif ch == 'G':
            val += 1
        skew.append(str(val))
    print(' '.join(skew))
if __name__ == '__main__':
    main(sys.argv[1:])