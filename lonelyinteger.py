#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    hm = {}
    for i in a:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    for key in hm:
        if hm[key] == 1:
            return key
