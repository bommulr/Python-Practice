def stringfun(l):
    new = ''

    for i in range(len(l)):
        new += l[i]
    return new

li =  ['a','b','c','de']
n = stringfun(li)
print(n)