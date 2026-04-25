def treatment(data):
    info = data.split()
    output = ""
    count = 1
    for i in range(len(info)-1):
        if info[i] == info[i+1]:
            count += 1
        else:
            output += str(info[i]) + "*" + str(count) + " "
            count = 1
    output += str(info[-1]) + "*" + str(count)
    return output

