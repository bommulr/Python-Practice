def count(str1):
    count = 0

    a = input('Give a alphabet to get the number of occurences:')

    for i in range(len(str1)):

        if str1[i] == a:
            count += 1
        
    print(count)

count('aaabbbcccdddd')