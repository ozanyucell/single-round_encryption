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
