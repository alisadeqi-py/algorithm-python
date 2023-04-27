from string import ascii_letters


def cipher(letter):
    
    new_word = ''
    for i in letter:
        
        ch = (ascii_letters.index(i) + 4 % len(ascii_letters) )
        new_word += ascii_letters[ch]
    return new_word


print(cipher('amir'))

