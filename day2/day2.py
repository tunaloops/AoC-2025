
result = []
with open('input.txt', 'r', encoding="utf-8") as f:
    read_data=f.read().strip('\n').split(",")
for i in read_data:
    i = i.split('-')
    x = int(i[0])
    y = int(i[1])
    check = range(x, y+1)
    for n in range(x, y+1):
        n = str(n)
        length = (len(n))
        mid = length // 2
        if length % 2 == 1:
            continue
        else:
            part1 = n[:mid]
            part2 = n[mid:]
            if part1 == part2:
                result.append(int(n))
a = sum(result)
print(a)    