import sys
def main(argv):
    text = argv[0]
    len_text = len(text)
    k = int(argv[1])
    freq_patterns = {}
    for idx in range(0,len_text-k+1):
        pattern = text[idx:idx+k]
        if pattern in freq_patterns.keys():
            freq_patterns[pattern] = freq_patterns[pattern] + 1
        else:
            freq_patterns[pattern] = 1
    max_count = 0
    for key in freq_patterns.keys():
        if freq_patterns[key] > max_count:
            max_count = freq_patterns[key]
    max_patterns = []
    for key in freq_patterns.keys():
        if freq_patterns[key] == max_count:
            max_patterns.append(key)
    print(max_patterns)

if __name__ == "__main__":
    main(sys.argv[1:])
                