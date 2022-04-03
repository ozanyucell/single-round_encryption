class Crypto:
    @staticmethod
    def encode(text, encode_key):
        split_text = Crypto.split_by_eight(text)
        if len(split_text[-1]) != 8:
            split_text[-1] += " " * (8 - len(split_text[-1]))
        swapped_words = []
        for word in split_text:
            new_word = ""
            for key_i in encode_key:
                new_word += word[key_i - 1]
            swapped_words.append(new_word)

        swapped_str = ''.join(swapped_words)
        encoded_str = ""
        for char in swapped_str:
            encoded_str += Crypto.char_to_binary[char]
        return encoded_str

    @staticmethod
    def decode(text, decode_key):
        decoded_words = []

        binary_chars = Crypto.split_by_eight(text)
        binary_decoded = ""
        for binary in binary_chars:
            binary_decoded += Crypto.binary_to_char[binary]

        split_text = Crypto.split_by_eight(binary_decoded)
        for word in split_text:
            new_word = ""
            for key_i in decode_key:
                new_word += word[key_i - 1]
            decoded_words.append(new_word)
        return ''.join(decoded_words).strip()

    @staticmethod
    def split_by_eight(text):
        return [text[i:i + 8] for i in range(0, len(text), 8)]


if __name__ == '__main__':
    plain_text = "Therefore the bananas are always before, that time will not be successful."
    perm_encode = [6, 4, 2, 8, 7, 5, 3, 1]
    perm_decode = [8, 3, 7, 2, 6, 1, 5, 4]

    print(f'  Plain: {plain_text}')
    encoded_text = Crypto.encode(plain_text, perm_encode)
    print(f'Encoded: {encoded_text}')
    decode_text = Crypto.decode(encoded_text, perm_decode)
    print(f'Decoded: {decode_text}')
