import difflib

# 九个情况的文本对
text_pairs = [
    ("这是一段完全相同的文本，没有任何差异。", "这是一段完全相同的文本，没有任何差异。"),
    ("这是一段从头开始就完全相同的文本，直到这个词的结尾。但是在这之后，文本1有额外的内容。",
     "这是一段从头开始就完全相同的文本，直到这个词的结尾。"),
    ("这是一段从头开始就完全相同的文本，直到这个词的结尾。",
     "这是一段从头开始就完全相同的文本，直到这个词的结尾。但是在这之后，文本2有额外的内容。"),
    ("在这之前，文本1有额外的内容。开始就完全相同的文本，直到最后一个字。",
     "开始就完全相同的文本，直到最后一个字。"),
    ("开始就完全相同的文本，直到最后一个字。",
     "在这之前，文本2有额外的内容。开始就完全相同的文本，直到最后一个字。"),
    ("文本1有多余的内容。完全相同的文本，直到最后。而在文本1的结尾还有额外的内容。",
     "完全相同的文本，直到最后。"),
    ("完全相同的文本，直到最后。",
     "文本2有多余的内容。完全相同的文本，直到最后。而在文本2的结尾还有额外的内容。"),
    ("文本1有自己的开始，然后就有完全相同的文本内容。",
     "完全相同的文本内容。文本2有自己的结束。"),
    ("完全相同的文本内容。文本1有自己的结束。",
     "文本2有自己的开始，然后就有完全相同的文本内容。")
]

# 对比差异并生成差异结果文本
diff_texts = []
for text1, text2 in text_pairs:
    d = difflib.Differ()
    diff = d.compare(text1, text2)
    diff_text = ''.join(diff)
    diff_texts.append(diff_text)

# 分裂带有差异标记的文本回text1和text2
split_text1 = []
split_text2 = []
for diff_text in diff_texts:
    lines = diff_text.split('\n')
    text1 = ''
    text2 = ''
    for line in lines:
        if line.startswith('- '):
            text1 += line[2:]
        elif line.startswith('+ '):
            text2 += line[2:]
        elif line.startswith('  '):
            text1 += line[2:]
            text2 += line[2:]
    split_text1.append(text1)
    split_text2.append(text2)

# 输出分割后的文本
for t1, t2 in zip(split_text1, split_text2):
    print("Text1:")
    print(t1)
    print("Text2:")
    print(t2)
    print("-------------------")
