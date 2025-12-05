from itertools import groupby

with open("test.txt", "r", encoding="utf-8") as f:
    read_data = f.read().splitlines()


def split_list(lst, val):
    return [list(group) for k, group in groupby(lst, lambda x: x == val) if not k]

lines = split_list(read_data, "")
fresh_ids = lines[0]
available_ids = lines[1]

def split_id(id_range, delimiter):
    return id_range.split(delimiter)

fresh = [] 
for id in fresh_ids:
    x = split_id(id, "-")[0]
    y = split_id(id, "-")[1]
    for i in available_ids:
        if int(i) >= int(x) and int(i) <= int(y):
            if (int(i)) in fresh:
                continue
            else:
                fresh.append(int(i))

print(len(fresh))
