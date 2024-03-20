# import difflib

# def map_diff_indices(text1, text2, opcodes):
#     indices_map = []
#     for tag, i1, i2, j1, j2 in opcodes:
#         if tag == 'equal':
#             for i in range(i1, i2):
#                 indices_map.append((i, i))
#         elif tag in ('delete', 'replace'):
#             for i in range(i1, i2):
#                 indices_map.append((i, None))
#         elif tag in ('insert', 'replace'):
#             for j in range(j1, j2):
#                 indices_map.append((None, j))
#     return indices_map

# text1 = "1镜片应贮存于无腐蚀气体环境中，贮存温度5~30℃、相对湿度40~了0%"
# text2 = "镜片应贮存于无腐蚀气体环境中，贮存温度5～30℃、相对湿度40～70%"
# d = difflib.SequenceMatcher(None, text1, text2)
# opcodes = d.get_opcodes()
# indices_map = map_diff_indices(text1, text2, opcodes)

# # 打印原始文本的位置映射
# print(indices_map)

# # ['  镜', '  片', '  应', '  贮', '  存', '  于', '  无', '  腐', '  蚀', '  气', '  体', '  环', '  境', '  中', '  ，', '  贮', '  存
# # ', '  温', '  度', '  5', '- ~', '+ ～', '  3', '  0', '  ℃', '  、', '  相', '  对', '  湿', '  度', '  4', '  0', '- ~', '- 了', '+ 
# # ～', '+ 7', '  0', '  %']


# import re

# # 假设para_stream_list是你的列表
# para_stream_list = ["xxxxxxxxxx。yyyyyyyyyyyy。", "zzzzzzzzz。aaaaaaa。"]

# # 分割字符串
# new_para_stream_list = []
# for para in para_stream_list:
#     sentences = re.split(r'(?<=[。！？])', para)
#     # 去掉空字符串
#     sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
#     # 加上前一句的结尾符
#     # for i in range(1, len(sentences)):
#     #     if sentences[i-1] and (sentences[i-1][-1] == '。' or sentences[i-1][-1] == '！' or sentences[i-1][-1] == '？'):
#     #         sentences[i] = sentences[i-1][-1] + sentences[i]
#     # 添加到新的列表中
#     new_para_stream_list.extend(sentences)

# # 打印结果
# for para in new_para_stream_list:
#     print(para)

import keyboard
import time
from datetime import datetime

log_file = 'key_log.txt'

def on_key_event(e):
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'按键：{e.name}，按键码：{e.scan_code}\n')

keyboard.hook(on_key_event)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    timestamp = time.time()
    local_time = datetime.fromtimestamp(timestamp)
    formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f'{formatted_time}')
finally:
    keyboard.unhook_all()

