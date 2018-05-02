import cv2

filepath = "img/11.png"
img = cv2.imread(filepath)  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
x = y = 10  # 坐标
w = 100  # 矩形大小（宽、高）
color = (0, 0, 255)  # 定义绘制颜色
cv2.rectangle(img, (x, y), (x + w, y + w), color, 1)  # 绘制矩形
cv2.imshow("Image", img)  # 显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有的窗体资源