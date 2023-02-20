def transpose(ins):
    if isinstance(ins[0], int):
        res = [list(map(int, str(num))) for num in ins]
        print(res)
    else:
        res = []
        temp = []
        counter = 0
        while ins:
            for el in ins:
                temp.append(el[counter])
            counter += 1
            res.append(temp)
            temp = []
            if len(res[0]) == len(ins) and len(res) == len(ins[0]):
                break
        print(res)


transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]])

# [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])
