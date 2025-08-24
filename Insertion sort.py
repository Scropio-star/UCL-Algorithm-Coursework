def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

if __name__ == '__main__':
    array = [5,4,3,2,1]
    print(insertionSort(array)) #output should be [1, 2, 3, 4, 5]