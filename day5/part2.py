from itertools import groupby

with open("input.txt", "r", encoding="utf-8") as f:
    read_data = f.read().splitlines()


def split_list(lst, val):
    return [list(group) for k, group in groupby(lst, lambda x: x == val) if not k]

lines = split_list(read_data, "")
fresh_str = lines[0]
fresh_ids = []
# convert the list(str) to a list of tuples(int)
for f_str in fresh_str:
    start, end = map(int, f_str.split("-"))
    fresh_ids.append((start, end))

fresh = 0 
current_max = 0
fresh_ids.sort(key=lambda x: x[0])

for x, y in fresh_ids:
    if y >= current_max:
        fresh += y - max(x, current_max) +1
        current_max = y + 1
print(fresh)
