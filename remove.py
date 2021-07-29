test_list = [5, 6,'','2','a', [], 3, [], [], 9]


final = []

for i in range(len(test_list)):

    if test_list[i] == '' or test_list[i] == []:
        continue
    else:
        final.append(test_list[i])
print(final)