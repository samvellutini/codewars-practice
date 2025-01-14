import sys
import os


with open ('prob06/input.txt', 'r') as file: 

    text = file.readlines()

    nums = int(text[0].strip())
    for i in range(1, nums + 1):        
        parts = text[i].split()

        age_in_months = int(parts[1])*12 +int(parts[2])

        answer = 25*12 - age_in_months
        
        print(parts[0],answer)
