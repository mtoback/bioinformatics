import sys
def main(pattern):
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
    output_str_len = len(output_str)
    f = open('temp.txt','w')
    if output_str_len < 80:
        f.write(output_str)
    else:
        pages = int(1+ output_str_len/80)
        for idx in range(0,pages):
            f.write(output_str[idx*80:idx*80+80])
    f.close()
    
if __name__ == "__main__":
    main(sys.argv[1])
