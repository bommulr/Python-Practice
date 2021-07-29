def sumofeven(lis):

    sum = 0

    for i in lis:
        if i%2 == 0:
            sum = sum+i
        continue
    return sum

total = sumofeven(lis=[1,2,3,6,8,5,4])
print(total)