import cv2
import numpy as np
import ujson as json
import os

def draw_boxes_on_image(image_path, data):
    # 读取图像
    img = cv2.imread(image_path)
    # 遍历data中的所有文本块
    for idx, item in enumerate(data):
        box = np.array(item['box'], dtype=np.int32)
        score = item['score']
        # 根据score值确定边框颜色
        if score < 0.8:
            color = (0, 0, 200)  # 红色
            cv2.putText(img, str(score), (box[1][0]-20, box[1][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (55, 55, 225), 1)
        elif 0.8 <= score < 0.9:
            color = (0, 200, 200)  # 黄色

        elif 0.9 <= score < 0.95:
            color = (0, 200, 0)  # 黄色
        else:
            color = (150, 150, 0)  # 绿色

        # 画出边框
        cv2.polylines(img, [box], isClosed=True, color=color, thickness=2)
        # 在边框左上角标注索引值
        cv2.putText(img, str(idx), (box[0][0], box[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (55, 55, 225), 2)

    # 显示处理后的图像
    cv2.imshow("solid_image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存处理后的图像
    cv2.imwrite("temp\\solid_image.jpg", img)

with open("temp\\data.txt", "r") as file:
    data_dict = json.load(file)


draw_boxes_on_image(f"{os.path.dirname(os.path.abspath(__file__))}\\temp\\test5.jpg", data_dict)
