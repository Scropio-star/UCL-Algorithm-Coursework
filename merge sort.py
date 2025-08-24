def merge(arr,low,mid,high):
    i, j, k= 0, 0, low #左右两个小数组的起点，以及合并的起点
    left_arr = arr[low:mid+1]
    right_arr = arr[mid+1:high+1] #创建新数组储存原数组，防止出现问题
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i+= 1
        else:
            arr[k] = right_arr[j]
            j+= 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k +=1
def sort(arr,low,high):
    if low < high:
        mid = low + (high - low) // 2
        sort(arr,low,mid)
        sort(arr,mid+1,high)
        merge(arr,low,mid,high)
if __name__ == '__main__':
    arr = [2,4,7,6,0,999,55]
    sort(arr,0,len(arr)-1)
    print(arr)
