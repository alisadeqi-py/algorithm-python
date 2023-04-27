


def encode(char):

    return [ord(i) for i in char]

def decode(list):

    return ''.join(chr(elm) for elm in list)

print(encode('ali'))

print(decode([97, 108, 105]))