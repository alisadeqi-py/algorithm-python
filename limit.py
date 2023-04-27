

def limit(arr , max=None , min=None):

    min_check = lambda val: True if min == None else (val >= min) 
    max_check = lambda val: True if max == None else (val<= max)

    return [val for val in arr if min_check(val) and max_check(val)]


print(limit([1,2,3,4,5] , 3))