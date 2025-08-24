import random
def partition(arr, low, high):
    i = low
    j = high + 1
    pivot = arr[i]
    while True:
        while True:
            i += 1
            if i >= high or arr[i] >= pivot:
                break
        while True:
            j -= 1
            if j == low or arr[j] <= pivot :
                break
        if i >= j :
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low],arr[j] = arr[j], arr[low]
    return j

def sort(arr, low, high):
    if low >= high:
        return
    j = partition(arr, low, high)
    sort(arr, low, j - 1)
    sort(arr, j + 1, high)

if __name__ == '__main__':
    arr = [5,4,3,2,7,9,10,11]
    random.shuffle(arr)
    sort(arr, 0, len(arr) - 1)
    print(arr)
