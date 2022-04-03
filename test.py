def test():
    right_rotated_block = [['01100000', '01000000', '00100000', '10000000', '01110000', '01010000', '00110000', '00010000'], ['01100000', '01000000', '00100000', '10000000', '01110000', '01010000', '00110000', '00010000']]

    for set_of_eight in right_rotated_block:
        index=0
        while index < len(set_of_eight):
            left_nibble = set_of_eight[index]
            right_nibble = set_of_eight[index+1]
            print(left_nibble,"-", right_nibble)
            if index==7: break
            index+=2
        return left_nibble, right_nibble


def main():
    left_nibble, right_nibble = test()
    print(left_nibble)
    print(right_nibble)
    
if __name__ == "__main__":
    main()
