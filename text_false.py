# 定义句子和字典A
sentence = '模拟使用状态下，光透过率在标准照明体D65和A下分别测定，其结果应 都是≥89%，模拟使用状态下，光透过率在标准照明体D65和A下分别测定，其结果应 都是≥89%'
dictionaryA = {'准': ['推'], '丙': ['内'], '≥': ['三'], '灰': ['炭'], '磷': ['麟'], '≥8': ['学'], '～': ['~~', '~'], '7': ['了'], '(': ['（'], ')': ['）'], '及': ['皮', '笈'], 'D': ['L']}

# 初始化字典B为空字典
dictionaryB = {}

# # 遍历句子，查找字典A的键，并记录索引位置到字典B中
# for index, char in enumerate(sentence):
#     for key in dictionaryA.keys():
#         if sentence[index:index+len(key)] == key:
#             if key not in dictionaryB:
#                 dictionaryB[key] = [index]
#             else:
#                 dictionaryB[key].append(index)

# # 输出字典B
# print(dictionaryB)

# # 遍历句子，查找字典A的键，并记录索引位置到字典B中
# for start_index in range(len(sentence)):
#     for end_index in range(start_index + 1, len(sentence) + 1):
#         substring = sentence[start_index:end_index]
#         if substring in dictionaryA:
#             if substring not in dictionaryB:
#                 dictionaryB[substring] = [(start_index, end_index - 1)]
#             else:
#                 dictionaryB[substring].append((start_index, end_index - 1))

# # 输出字典B
# print(dictionaryB)

# 遍历句子，查找字典A的键，并记录索引位置到字典B中
for start_index in range(len(sentence)):
    for end_index in range(start_index + 1, len(sentence) + 1):
        substring = sentence[start_index:end_index]
        if substring in dictionaryA:
            if len(substring) == 1:
                if substring not in dictionaryB:
                    dictionaryB[substring] = [start_index]
                else:
                    dictionaryB[substring].append(start_index)
            else:
                if substring not in dictionaryB:
                    dictionaryB[substring] = [(start_index, end_index - 1)]
                else:
                    dictionaryB[substring].append((start_index, end_index - 1))

# 输出字典B
print(dictionaryB)
