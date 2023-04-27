

def check(letter1 , letter2):

    dic = {}
    pack = zip(letter1, letter2)
    for i,j in pack:
        print(dic.keys())
        print(j,i)
        if i  in dic:
            if dic[i] != j:
                return False
        if j in dic:
            if dic[j] != i:
                return False
            
        if i not in dic.keys():
            dic[i] = j
    return True , dic
    
print(check('foo' , 'ber'))