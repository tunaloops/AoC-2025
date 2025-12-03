with open("input.txt", 'r', encoding="utf-8") as f:
    read_data = f.read().splitlines()


res = []
# greedy algo
for line in read_data:
    digits = [int(x) for x in line]
    num = []
    start_pos = 0
    max_range= 12
    for pick_number in range(max_range):
        current_index = len(digits) - max_range
        substring = digits[start_pos:current_index+1]
        max_num = max(substring)
        start_pos += (substring.index(max_num)+1)
        num.append(max_num)
        max_range-=1     
    x = int("".join(map(str, num)))
    res.append(x)
    
print(sum(res))