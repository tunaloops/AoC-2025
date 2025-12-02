def check_pattern(number_string, pattern_length):
    # Extract the pattern (first chunk)
    pattern = number_string[:pattern_length]
    check = []
    for i in range(0, len(number_string), pattern_length):
    	chunk = number_string[i:i+pattern_length]
    	if pattern == chunk:
    		check.append("t")
    	else:
    		check.append("f")
    if check.count("f") == 0:
    	return True
    else:
        return False





result = []
with open('input.txt', 'r', encoding="utf-8") as f:
    read_data=f.read().strip('\n').split(",")
for i in read_data:
    i = i.split('-')
    x = int(i[0])
    y = int(i[1])
    for n in range(x, y+1):
        n = str(n)
        length = (len(n))
        possible_pattern_lengths = length // 2
        for j in range(1, possible_pattern_lengths+1):
            x = check_pattern(n, j)
            if x == True:
                result.append(int(n))
                break
                

print(sum(result))
