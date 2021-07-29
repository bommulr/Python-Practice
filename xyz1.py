## Program to remove empty lists, dicts, strings in a given list ##

test_list = {"a":[5, 6,'','2','a', [], 3, [], [], 9, {}] ,"b":[], "c":{"d":[] ,"e":[1,2] } }

x = list(test_list.values())
modified = []
for i in range(len(x)):
    
    if type(x[i]) == list:
        for j in range(len(x[i])):
            if x[i][j] == [] or x[i][j] == '' or x[i][j] == {}:
                continue
            else:
                modified.append(x[i][j])

    if type(x[i]) == dict:
        for a in list(x[i].values()):
            if a == {} or a == [] or a == '':
                continue
            else:
                modified.append(a)
print(modified)
