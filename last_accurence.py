


array  = [1,2,3,4,5,5,5,5,6,6,6,7,8,9,10,10,10,11,12,13,14,15,16,17]


def last_occurence(array , element):

    low , high = 0 , len(array)-1

    while low <= high:
        mid = (low + high) //2
        val = array[mid]

        if (val == element and mid == len(array)-1) or (val == element and array[mid + 1] > element):
            return mid
         
        elif val <= element:

            low = mid +1
        else:

            high = mid - 1

print(last_occurence(array , 6))