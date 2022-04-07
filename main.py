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

binary_to_char =   {'00000001': 'A', '00000010': 'B', '00000011': 'C', '00000100': 'Ç', '00000101': 'D',
                    '00000110': 'E', '00000111': 'F', '00001000': 'G', '00001001': 'Ğ', '00001010': 'H',
                    '00001011': 'I', '00001100': 'İ', '00001101': 'J', '00001110': 'K', '00001111': 'L',
                    '00010000': 'M', '00010001': 'N', '00010010': 'O', '00010011': 'Ö', '00010100': 'P',
                    '00010101': 'R', '00010110': 'S', '00010111': 'Ş', '00011000': 'T', '00011001': 'U',
                    '00011010': 'Ü', '00011011': 'V', '00011100': 'Y', '00011101': 'Z', '00011110': 'Q',
                    '00011111': 'W', '00100000': 'X', '00100001': '.', '00100010': ',', '00100011': '(',
                    '00100100': ')', '00100101': '!', '00100110': ';', '00100111': ':', '00101000': "'",
                    '00101001': '"', '00101010': '-', '00101011': '?', '00101100': '$', '00101101': '@',
                    '00101110': '%', '00101111': ' ', '10000001': 'a', '10000010': 'b', '10000011': 'c',
                    '10000100': 'ç', '10000101': 'd', '10000110': 'e', '10000111': 'f', '10001000': 'g',
                    '10001001': 'ğ', '10001010': 'h', '10001011': 'ı', '10001100': 'i', '10001101': 'j',
                    '10001110': 'k', '10001111': 'l', '10010000': 'm', '10010001': 'n', '10010010': 'o',
                    '10010011': 'ö', '10010100': 'p', '10010101': 'r', '10010110': 's', '10010111': 'ş',
                    '10011000': 't', '10011001': 'u', '10011010': 'ü', '10011011': 'v', '10011100': 'y',
                    '10011101': 'z', '10011110': 'q', '10011111': 'w', '10100000': 'x'}

def file_reader():
    with open(f"C:\\Users\\ozany\\Desktop\\test.txt", mode='r', encoding='utf-8') as file:
        text = file.read()

    block_list = []

    block_list = split_by_eight(text)
    return block_list

def split_by_eight(text):
    return [text[i:i + 8] for i in range(0, len(text), 8)]

def permutation(block_list):
    for content in block_list:
        temp_list = list(content)

        # "ABCÇDEFG", "ABCÇDEFG"

        temp_list[0], temp_list[7] = temp_list[7], temp_list[0] # 82345671
        temp_list[5], temp_list[0] = temp_list[0], temp_list[5] # 62345871
        temp_list[2], temp_list[5] = temp_list[5], temp_list[2] # 62845371
        temp_list[1], temp_list[2] = temp_list[2], temp_list[1] # 68245371
        temp_list[1], temp_list[3] = temp_list[3], temp_list[1] # 64285371
        temp_list[4], temp_list[5] = temp_list[5], temp_list[4] # 64283571
        temp_list[4], temp_list[6] = temp_list[6], temp_list[4] # 64287531

        new_text = ""

        for character in temp_list: 
            new_text = new_text + character

        block_list[block_list.index(content)] = new_text

    return block_list

'''
def reverse_permutation(block_list):
    for content in block_list:
        temp_list = list(content)

        temp_list[0], temp_list[7] = temp_list[7], temp_list[0] # 82345671
        temp_list[5], temp_list[0] = temp_list[0], temp_list[5] # 62345871
        temp_list[2], temp_list[5] = temp_list[5], temp_list[2] # 62845371
        temp_list[1], temp_list[2] = temp_list[2], temp_list[1] # 68245371
        temp_list[1], temp_list[3] = temp_list[3], temp_list[1] # 64285371
        temp_list[4], temp_list[5] = temp_list[5], temp_list[4] # 64283571
        temp_list[4], temp_list[6] = temp_list[6], temp_list[4] # 64287531

        new_text = ""

        for character in temp_list: 
            new_text = new_text + character

        block_list[block_list.index(content)] = new_text

    return block_list
'''

def set_alphabet():
    characters= "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ.,()!;:'\"-?$@%abcçdefgğhıijklmnoöprsştuüvyzQWXqwx"
    return characters

def binary_counter():
    num = 1
    encoded_characters = {}

    for character in set_alphabet():
        encoded_characters[character] = f'{num:08b}'
        num+=1
    return encoded_characters

def encoder(text_list):
    block_binary_list = []

    for i in text_list:
        temp_list = list(i)
        for character in temp_list:
            temp_list[temp_list.index(character)] = char_to_binary[character]

        block_binary_list.append(temp_list)

    return block_binary_list

def decoder(block_list):
    decoded_text = ""
    for set_of_8 in block_list:
        for char in set_of_8:
            decoded_text = decoded_text + binary_to_char[char]
    return decoded_text

def shift_right_rotation(times, block_binary_list):
    output = []
    for block in block_binary_list:
        inner_output = []

        for data in block:
            temp_list = list(data)

            for i in range(times):
                temp_list.insert(0, temp_list.pop())
                        
            binary_text= ""
            for character in temp_list:
                binary_text += character

            inner_output.append(binary_text)

        output.append(inner_output)
    print(output)
    return output

def shift_left_rotation(times, block_binary_list):
    output = []
    for block in block_binary_list:
        inner_output = []

        for data in block:
            temp_list = list(data)

            for i in range(times):
                temp_list.append(temp_list.pop(0))
                        
            binary_text= ""
            for character in temp_list:
                binary_text = binary_text + character

            inner_output.append(binary_text)

        output.append(inner_output)

    return output

def encryption(plain_text):
    block_list = permutation(plain_text)
    block_binary_list = encoder(block_list)

    right_rotated_block = shift_right_rotation(4, block_binary_list)

    block = nibble_handler(right_rotated_block)

    return decoder(block)

def nibble_handler(block):
    # [['01100000', '01000000', '00100000', '10000000', '01110000', '01010000', '00110000', '00010000'], ['01100000', '01000000', '00100000', '10000000', '01110000', '01010000', '00110000', '00010000']]
    K2, K3, K4, K5 = key_generator()
    left_nibble = []
    right_nibble = []
    for set_of_eight in block:
        for i in range(0, len(set_of_eight), 2):
            left_nibble.append(set_of_eight[i])
            right_nibble.append(set_of_eight[i+1])

        for i in range(len(left_nibble)):
            left_nibble[i] = xor(left_nibble[i], K2)
            right_nibble[i] = xor(right_nibble[i], K3)
        
        for i in range(len(left_nibble)):
            left_nibble[i] = xor(left_nibble[i], K4)
            right_nibble[i] = xor(right_nibble[i], K5)

        for i in range(0, len(left_nibble), 2):
            block[block.index(set_of_eight)][i] = left_nibble[i]
            block[block.index(set_of_eight)][i+1] = right_nibble[i]

    return block

def key_generator():
    key = "AB"

    encoded_key = two_bit_encoder(key)

    column0 = [encoded_key[0], encoded_key[4], encoded_key[8], encoded_key[12]]
    column1 = [encoded_key[1], encoded_key[5], encoded_key[9], encoded_key[13]]
    column2 = [encoded_key[2], encoded_key[6], encoded_key[10], encoded_key[14]]
    column3 = [encoded_key[3], encoded_key[7], encoded_key[11], encoded_key[15]]

    K2, K3 = concatenate_columns(column0, column1, column2, column3)

    K2 = xor(K2[0], K2[1])
    K3 = xor(K3[0], K3[1])

    K4 = keySLR(3, K2)
    K5 = keySRR(3, K3)

    return K2, K3, K4, K5

def two_bit_encoder(string_key):
    encoded_key=""
    for character in list(string_key):
        encoded_key = encoded_key + char_to_binary.get(character)
    
    '''
    encoded_key = 0000000100000010 #(00000001, 00000010)
       0 1 2 3
    0| 0 0 0 0
    1| 0 0 0 1
    2| 0 0 0 0
    3| 0 0 1 0
    '''
    return encoded_key

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

def concatenate_columns(column0, column1, column2, column3):
    conc_31 = ""
    conc_02 = ""
    conc_01 = ""
    conc_23 = ""

    for i in range(len(column3)):
        conc_31 += column3[i] + column1[i]
        conc_02 += column0[i] + column2[i]
        conc_01 += column0[i] + column1[i]
        conc_23 += column2[i] + column3[i]

    K2 = [conc_31, conc_02] # columns 3 1 = x | columns 0 2 = y
    K3 = [conc_01, conc_23] # columns 0 1 = x | columns 2 3 = y

    return K2, K3

def xor(key0, key1):
    XOR_key = ""
    
    for i in range(len(key0)):
        if key0[i] == key1[i]:
            XOR_key += "0"
        else:
            XOR_key += "1"
    return XOR_key

def decryption(cypher_text):
    return cypher_text

def main():
    plain_text = file_reader()
    print(plain_text)
    output = encryption(plain_text)

    print(output)

    '''
    cypher_text = encrypted_text
    decrypted_text = decryption(cypher_text)
    '''

if __name__ == "__main__":
    main()
