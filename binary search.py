from fileinput import close

low = 0
array = [1,2,3,4,5,6,7,8,9]
high = len(array)-1
given_number = int(input("Enter a number: "))
while low <= high:
    mid = low + (high-low)//2
    if array[mid] == given_number:
        print(f'The position of given number is {mid+1}')
        break
    elif array[mid] < given_number:
        low = mid + 1
    else :
        high = mid - 1
else:
    print('Not found')


