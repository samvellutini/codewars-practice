 
with open ('prob03/input.txt', 'r') as inputt: 
    num: int = 0
    text = inputt.readlines()
    for line in text:
        num_string = line.strip()
        num = int(num_string)
        if (num == -1):
            break
        print('You, ', end='')
        print(num_string, end='')
        if num == 1:
            print(" minute ago.")
        else:
            print(" minutes ago.")

