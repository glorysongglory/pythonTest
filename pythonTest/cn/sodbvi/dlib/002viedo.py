import cv2
import dlib

detector = dlib.get_frontal_face_detector()  #使用默认的人类识别器模型

'''
1.Dlib模型识别的准确率和效果要好于OpenCV；

2.Dlib识别的性能要比OpenCV差，使用视频测试的时候Dlib有明显的卡顿，但是OpenCV就好很多，基本看不出来；
'''

def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    for face in dets:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.imshow("image", img)


cap = cv2.VideoCapture(0)
while (1):
    ret, img = cap.read()
    discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
