from PPOCR_api import GetOcrApi

import os

# 测试图片路径
TestImagePath = f"{os.path.dirname(os.path.abspath(__file__))}\\temp\\20231010115506.png"

# 初始化识别器对象，传入 PaddleOCR-json.exe 的路径
path = os.path.join("D:", "Code", "PaddleOCR-json_v.1.3.0", "PaddleOCR-json.exe")
ocr = GetOcrApi(r"D:\Code\PaddleOCR-json_v.1.3.0\PaddleOCR-json.exe")
# exit()
print(f'初始化OCR成功，进程号为{ocr.ret.pid}')
print(f'\n测试图片路径：{TestImagePath}')

# 示例1：识别本地图片
res = ocr.run(TestImagePath)
# print(f'\n示例1-图片路径识别结果（原始信息）：\n{res}')
data = res['data']
# from pprint import pprint
# pprint(data)
# 将数据写入文本文件
import ujson as json
with open("temp\\data.txt", "w") as file:
    json.dump(data, file)

print(f'\n图片路径识别结果（格式化输出）：')
ocr.printResult(res)