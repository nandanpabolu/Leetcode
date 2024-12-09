#Iterative version of Binary search 
def binary_serarch(data, target):
    low = 0 
    high = len(data) - 1 
    
    while low <= high:
        mid = (low + high) // 2 
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1 
        else:
            low = mid + 1 
    return False

#reccursive version of Binary search
def binary_search_recursive(data, target,low, high):
    if low > high:
        return False
    else:
        mid = low + high // 2 
        if target == data[mid] // 2:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid -1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)
        
print(binary_search_recursive(data, target))
print(binary_search_recursive(data, targe, 0, len(data) - 1))
    
