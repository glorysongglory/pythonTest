import cv2
#参数0表示，获取第一个摄像头
cap = cv2.VideoCapture(0)
while (1):
    ret, img = cap.read()
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源