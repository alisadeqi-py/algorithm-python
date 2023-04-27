

def rotate(chr , time ):
    chr = list(chr)
    time = time + 1
    for i in range(0 , time):
        print(i)
        chr[i] = chr[-i]
    chr = ''.join(chr)
    return chr


""" time =  2 + 1
for i in range(1 , time):
    print(i) """

print(rotate('hello' ,2))
