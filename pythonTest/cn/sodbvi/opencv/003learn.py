import cv2

filepath = "img/11.png"
img = cv2.imread(filepath)  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色

# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier("D:\pycharm\pythonTest\pythonTest\cn\sodbvi\opencv\data\haarcascade_frontalface_default.xml")
color = (0, 0, 255)  # 定义绘制颜色
# 调用识别人脸
'''
分类器classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))参数说明：

gray：转换的灰图

scaleFactor：图像缩放比例，可理解为相机的X倍镜

minNeighbors：对特征检测点周边多少有效点同时检测，这样可避免因选取的特征检测点太小而导致遗漏

minSize：特征检测点的最小尺寸
'''

faceRects = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)

cv2.imshow("image", img)  # 显示图像
c = cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()