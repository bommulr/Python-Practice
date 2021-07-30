def prime(list1):
    total = 0

    for i in list1:

        for j in range(3,i):

            if i%j == 0:

                break
            else:

                total+=1
                

    print(total)













prime([3,4,5,6,7,8,9,10,11,12])