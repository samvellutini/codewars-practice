with open ('prob14/input.txt', 'r') as file:
    text = file.readline()
    check = file.readline()
    check = float (check.strip('CheckSum='))

    
    
    print(sum)
    list = text.split()
 
    for i in range(len(list)-1, -1, -1):
        try:
            list[i] = float (list[i])
        except:
            list.pop(i)
    print(" ".join(map(str, list)))
    sum = 0
    for i in range(len(list)):
        sum+=list[i]
    if sum == check:
        print("CHECKED")
    else:
        print("BADCHECK")