def binarySearch(arr,is_ascending, x):
    low,high = 0, len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x if is_ascending else arr[mid] > x:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1
def findpeak(arr):
    low,high = 0, len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low
array = [2,4,6,8,10,12,11,9,7,5,3,1,0]
maxIndex = findpeak(array)
increasing_part = array[:maxIndex+1]
decreasing_part = array[maxIndex:]
given_number = int(input('Enter the number: '))
idx = binarySearch(increasing_part,True, given_number)
if idx != -1:
    print(f'found at index {idx} at the increasing part', )
else:
    idx = binarySearch(decreasing_part, False, given_number)
    actual_index = maxIndex + idx
    if idx != -1:
        print(f'found at index {actual_index} at the decreasing part')
    else:
             print("Not found")


