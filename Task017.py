# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

input = [1, 1, 2, 0, -1, 3, 4, 4]
counts = {}
for i in input:
    if counts.__contains__(i):
        counts[i] += 1
    else:
        counts[i] = 1
print(len(counts))
# for k,v in counts.items():
#     (print(f"{k} - {v}"))
# for k in counts:
#     (print(f"{k} - {counts[k]}"))
