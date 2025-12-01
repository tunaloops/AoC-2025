import re

dial = 50
result = []
zero_counter = 0
regexL = "L\d+"
regexR = "R\d+"
with open('input.txt', 'r', encoding="utf-8") as f:
    read_data = f.read().splitlines()
for x in read_data:
    if (re.fullmatch(regexL, x)):
        number = int(x.strip("L"))
        while number > 0:
            dial = (dial - 1) % 100 # decrement and wrap
            if dial == 0:
                zero_counter+=1
            number-=1    
        result.append(dial) 
    elif (re.fullmatch(regexR, x)):
        number = int(x.strip("R"))   
        while number > 0:
            dial = (dial + 1) % 100 # increment and wrap
            if dial == 0:
                zero_counter+=1
            number-=1
        result.append(dial)              
print(result.count(0)) # part 1
print(zero_counter) # part 2


