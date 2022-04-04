'''
char_to_binary =   {'A': '00000001', 'B': '00000010', 'C': '00000011', 'Ç': '00000100', 'D': '00000101',
                    'E': '00000110', 'F': '00000111', 'G': '00001000', 'Ğ': '00001001', 'H': '00001010',
                    'I': '00001011', 'İ': '00001100', 'J': '00001101', 'K': '00001110', 'L': '00001111',
                    'M': '00010000', 'N': '00010001', 'O': '00010010', 'Ö': '00010011', 'P': '00010100',
                    'R': '00010101', 'S': '00010110', 'Ş': '00010111', 'T': '00011000', 'U': '00011001',
                    'Ü': '00011010', 'V': '00011011', 'Y': '00011100', 'Z': '00011101', 'Q': '00011110',
                    'W': '00011111', 'X': '00100000', '.': '00100001', ',': '00100010', '(': '00100011',
                    ')': '00100100', '!': '00100101', ';': '00100110', ':': '00100111', "'": '00101000',
                    '"': '00101001', '-': '00101010', '?': '00101011', '$': '00101100', '@': '00101101',
                    '%': '00101110', ' ': '00101111', 'a': '10000001', 'b': '10000010', 'c': '10000011',
                    'ç': '10000100', 'd': '10000101', 'e': '10000110', 'f': '10000111', 'g': '10001000',
                    'ğ': '10001001', 'h': '10001010', 'ı': '10001011', 'i': '10001100', 'j': '10001101',
                    'k': '10001110', 'l': '10001111', 'm': '10010000', 'n': '10010001', 'o': '10010010',
                    'ö': '10010011', 'p': '10010100', 'r': '10010101', 's': '10010110', 'ş': '10010111',
                    't': '10011000', 'u': '10011001', 'ü': '10011010', 'v': '10011011', 'y': '10011100',
                    'z': '10011101', 'q': '10011110', 'w': '10011111', 'x': '10100000'}

def key_generator():
    key = "AB"

    encoded_key = two_bit_encoder(key)

    column0 = encoded_key[0] + encoded_key[4] + encoded_key[8] + encoded_key[12]
    column1 = encoded_key[1] + encoded_key[5] + encoded_key[9] + encoded_key[13]
    column2 = encoded_key[2] + encoded_key[6] + encoded_key[10] + encoded_key[14]
    column3 = encoded_key[3] + encoded_key[7] + encoded_key[11] + encoded_key[15]
    K2 = [column3 + column1, column0 + column2] # columns 3 1 0 2
    K3 = [column0 + column1, column3 + column2] # columns 0 1 3 2
    
    return K2

def two_bit_encoder(string_key):
    encoded_key=""
    for char in list(string_key):
        encoded_key = encoded_key + char_to_binary.get(char)
    
    \'''
    encoded_key = 0000000100000010 #(00000001, 00000010)
       0 1 2 3
    0| 0 0 0 0
    1| 0 0 0 1
    2| 0 0 0 0
    3| 0 0 1 0
    \'''
    return encoded_key
'''

def keySRR(times, key):
    rotated_key = ""
    
    temp_list = list(key)
    for i in range(times):
        temp_list.insert(0, temp_list.pop())

    for bit in temp_list:
        rotated_key = rotated_key + bit

    return rotated_key

def keySLR(times, key):
    rotated_key = ""
    temp_list = list(key)
    for i in range(times):
        temp_list.append(temp_list.pop(0))

    for bit in temp_list:
        rotated_key = rotated_key + bit

    return rotated_key

def main():
    test = '00100000'
    print(keySRR(3, test))
    print(keySLR(3, keySRR(3, test)))

if __name__ == "__main__":
    main()
