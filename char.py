 #!/usr/bin/python
 
secret = "53���305))6�;4826)4�.)4�);806�;48�8^60))85;161;:��8�83(88)5��;46(;88�96�?;8)��(;485);5��2:��(;4956�2(5��4)8^8�;4069285);)6�8)4��;1(�9;48081;8:8�1;48�85;4)485�528806�81(�9;48;(88;4(�?34;48)4�;1�(;:188;�?;"

char_dict = {}
unique_chars = set(list(secret))
for ch in unique_chars:
    char_dict[ch] = 0
for ch in list(secret):
    char_dict[ch] = char_dict[ch] + 1
len_sec = len_secret
for ch in char_dict.keys():
    print('%s : %f' % (ch, float(char_dict[ch]/len_sec)))