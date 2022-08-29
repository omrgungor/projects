# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]
def reverser(l):
    for i in l:
        i.reverse()
        l.reverse()
    return l
l = [[1, 2], [3, 4], [5, 6, 7]]
reverser(l)
print(l)
    






    


