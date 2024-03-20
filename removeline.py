import cv2
import numpy as np

def detect_lines(image, thickness=1, line_color=255):
    # 获取图像的高度和宽度
    pixel_height_line = image.shape[0]
    pixel_width_line = image.shape[1]

    # 记录横线的上下边界
    horizontal_lines = []

    # pixel_values = list(range(31))

    # 遍历图像的高度
    for height_x in range(0, pixel_height_line, thickness):
        count = 0
        # 检查横向连续的黑色像素长度
        for width_x in range(pixel_width_line - thickness + 1):
            # 如果当前位置及粗度范围内的像素都为黑色
            if np.all(np.any(image[height_x, width_x:width_x + thickness] == 0)):
                count += 1

            # 如果连续黑色像素长度超过当前粗度阈值的95%
            if count > int(pixel_width_line * 0.9):
                # 将该横向区域的像素值全部设为白色（255），去除横线
                image[height_x, :] = line_color
                # 记录横线的上下边界
                horizontal_lines.append([height_x, height_x + thickness - 1])
                break

    return image, horizontal_lines

# 读取彩色图像
image = cv2.imread('temp\\20231030092616.png')
# image = cv2.imread('temp\\6.png')

# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 设置灰度值在80以下的像素为0
gray_image[gray_image < 80] = 0

# 设置灰度值在210以上的像素为255
gray_image[gray_image > 210] = 255

_, gray_image = cv2.threshold(gray_image, 210, 255, cv2.THRESH_BINARY)

# 使用1像素的粗细进行横线检测
processed_image, horizontal_lines = detect_lines(gray_image.copy(), thickness=1, line_color=255)

# 使用1像素的粗细进行竖线检测
processed_image_vertical, vertical_lines = detect_lines(gray_image.copy().T, thickness=1, line_color=255)

# 将横线图像和竖线图像进行逻辑或运算，去除横线和竖线
final_image = cv2.bitwise_or(processed_image, processed_image_vertical.T)

# # 显示去除表格线后的图像
# cv2.imshow('Processed Image', final_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
