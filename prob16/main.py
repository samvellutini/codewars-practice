from collections import Counter
with open ('prob16/input.txt', 'r') as file:
    text = file.readlines()
    for i in range(len(text)):
        text[i] = (int) (text[i].strip('/n'))
    print(text)
    def numerate(j):
        count = 0
        stock = text[j]
        for i in range(len(text)):
            if text[i] == stock:
                count+=1
               # text.pop[i]
        print(count)


    trending = 0
    second_place = 0
    #numerate(1)
    print(Counter(text))

   ## for line in text:
     #   numerate(line)
    
        
