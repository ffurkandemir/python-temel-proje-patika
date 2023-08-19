list = [[1, 2], [3, 4], [5, 6, 7]]
new_list = []
temp_list = []
def reverse():
    index = []
    for count in range(len(list)):
        index.append(count)
    print(index)

    for i in list[::-1]:
        temp_list.append(i[::-1])
    print(temp_list)

reverse()
