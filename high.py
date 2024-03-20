# import random
# import string
from pprint import pprint

# # 生成随机文本，随机选择一些字母高亮
# def generate_random_text(length=20, highlight_probability=0.3):
#     text = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
#     highlighted_text = ''
#     for char in text:
#         if random.random() < highlight_probability:
#             highlighted_text += f'<span style="color: #55a6f7;">{char}</span>\n'
#         else:
#             highlighted_text += char
#     return text, highlighted_text

# # 生成字母列表，仅保留前5个字母
# def generate_letter_list(text):
#     letter_list = [char for char in text if char.isalpha()]
#     return list(set(letter_list))[:5]

# # 示例用法
# original_text, highlighted_text = generate_random_text()
# letter_list = generate_letter_list(original_text)

# print("Original Text:")
# print(original_text)
# print("\nHighlighted Text:")
# pprint(highlighted_text)
# print("\nLetter List (First 5 letters):")
# print(letter_list)

a = 'sadf<span style="color: #55a6f7;">o</span>\nlsdeb<span style="color: #55a6f7;">u</span>\n<span style="color: #55a6f7;">e</span>\nw<span style="color: #55a6f7;">s</span>\n<span style="color: #55a6f7;">i</span>\nj<span style="color: #55a6f7;">x</span>\nqc<span style="color: #55a6f7;">d</span>\ndqf<span style="color: #55a6f7;">e</span>\n'
b = ['l', 'c', 'f', 'o', 'j']

c = any('<span style="color: #55a6f7;">{}</span>'.format(key) in a for key in b) # false
d = all('<span style="color: #55a6f7;">{}</span>'.format(key) in a for key in b) # false
e = any('<span style="color: #55a6f7;">{}</span>'.format(key) not in a for key in b) # true
f = all('<span style="color: #55a6f7;">{}</span>'.format(key) not in a for key in b) # true

pprint(a)
print(c)
print(d)
print(e)
print(f)