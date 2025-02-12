import cv2

cascade = cv2.CascadeClassifier(r"C:\Users\PC\Desktop\python lesson\sample\haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\PC\Desktop\python lesson\sample\fg.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray, scaleFactor=1.01)


for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x + w, y + h),(0,0,255))

cv2.imwrite(r"C:\Users\PC\Desktop\python lesson\sample\fg1.jpg",img)