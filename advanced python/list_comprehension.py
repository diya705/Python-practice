myList = [1, 2, 9, 5, 3, 5]
squaredList = []   # squaredlist(write any name) is used  to square the values in the list
for item in myList:
    squaredList.append(item*item)


squaredList = [i*i for i in myList]  # also write this in this way and write in any way

print(squaredList)