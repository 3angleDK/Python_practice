# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

s = set()
for item in lst:
    for k, v in item.items():
        s.add(v)
print(s)
 
# res = {}
# for item in lst:
#     for k, v in item.items():
#         if res.__contains__(v):
#             res[v].append(k)
#         else:
#             res[v] = [k]
# # print(res)
# print(res.keys())