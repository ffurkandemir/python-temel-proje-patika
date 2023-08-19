list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list = []
def flatten():
    for index in range(len(list)):
        new_list.append(list[index])
flatten()
print(new_list)

    