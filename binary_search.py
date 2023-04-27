

array  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16 , 17]


def binary_search( array  , element ):
    low = 0
    high = len(array)-1

    while low <= high:
        mid = (low + high ) // 2
        val = array[mid]
        
        if val == element:
            return mid
        
        elif val < element:
            low = mid + 1 
        
        elif val > element:
            high = mid - 1 
               
               

    return -1

print(binary_search(array ,15))
        








































































