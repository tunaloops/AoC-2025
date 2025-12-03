with open("input.txt", 'r', encoding="utf-8") as f:
    read_data = f.read().splitlines()
sum = 0
rdi = None
rdx = None
num = 0
for i in read_data:
    digits = [int(x) for x in i]
    max_num = (max(digits))
    lcheck = 0
    rcheck = 0
    max_index = digits.index(max_num)
    rsublist = digits[max_index+1:] # sublist containing everything after and excluding max_num
    lsublist = digits[:max_index] # sublist containg everything before and excluding max_num
    if len(lsublist) != 0:
        lcheck = (max(lsublist))
    else:
        lcheck = None # not 0, because that messes up the math
    if len(rsublist) != 0:
        rcheck = max(rsublist)        
    else:
        rcheck = None # not 0, because that messes up the math
    if lcheck != None:
        rdi = int(str(lcheck) + str(max_num))
    else: # no need for comparison, take the l buddy
        num = int(str(max_num) + str(rcheck))
        sum += num
        continue
    if rcheck != None:
        rdx = int(str(max_num) + str(rcheck))
    else: # no need for comparison, take the l buddy
        num = int(str(lcheck) + str(max_num))
        sum+=num
        continue
    if rdi != None and rdx != None:
        if rdi > rdx: 
            num = rdi
        elif rdx > rdi:
            num = rdx
    sum += num
    

print(sum)    