## Function to reverse a string ##

def reverse(n):

    l = len(n)
    new = ''

    for i in range(l):
        new = new + n[(l-1)-i]
    return new

new_string = reverse('abcde')
print(new_string)
