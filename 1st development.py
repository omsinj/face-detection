""" the ability to identify human faces in digital images, this is not the same as face recognition
if you have a photograh, this application is able to tell you where the faces are and threw boxes around faces"""

# the algorithm use here is Haar Cascades or Deep Learning

# it can detect multiple faces in a photograph. 

pip install opencv-python

import cv2 

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # works with person facing frontal

photo = cv.imrad('file path')

grayscale_photo = cv.2cvtColor(photo, cv2.COLOR_BGR2GRAY)

cv2.imwrite('photo-grayscale.webp', grayscale_photo)

faces = face_classifier.detectMultiScale(grayscale_photo, scaleFactor = 1.1, 

for face_coords in faces:
  x,y,w,h = face_coords
  cv2.rectagle(group_photo (x,y), (x + w, y +h), (255, 0, 0))

cv2.imshow('Face Detection', photo)

cv2.waitkey(0)
cv2.destroyAllWindows()


