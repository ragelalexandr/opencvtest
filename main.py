import cv2
import numpy


# Работа с видео
cap = cv2.VideoCapture('videos/video.mp4')
while True:
    succses, img = cap.read()

    # Оттенки серого))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 80, 120)

    

    cv2.imshow('result', img)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

# #работа с картинками
# # img = cv2.imread("images/img89.jpg")
# # img = cv2.resize(img,(1800, 1400))

# #Оттенки серого))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #Контуры
# img = cv2.Canny(img, 60, 60)

# #Дополнительный контур, для замыкания контуров
# kernel = numpy.ones((5,5), numpy.uint8)
# img = cv2.dilate(img, kernel, iterations=1)

# img = cv2.erode(img, kernel, iterations=1)




# # Размытие
# # img = cv2.GaussianBlur(img,(9, 9), 0)

# # Часть картинки
# # cv2.imshow('result', img[0:50, 0:50])

# cv2.imshow('result', img)
# print(img.shape)
# cv2.waitKey(0)