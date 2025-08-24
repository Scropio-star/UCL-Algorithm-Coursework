stairsCost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
step = len(stairsCost)
index = 0
total = 0
while index < step-1:
    if stairsCost[index+1] > stairsCost[index + 2]:
        total += stairsCost[index + 2]
        index+=2
    else:
        total += stairsCost[index + 1]
        index +=1
print(total)