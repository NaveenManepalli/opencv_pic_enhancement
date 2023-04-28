import cv2


n = input("Enter the image number:")


img = cv2.imread(n + '.jpg', cv2.IMREAD_GRAYSCALE)


img_blur = cv2.GaussianBlur(img, (5, 5), 0)


img_usm = cv2.addWeighted(img, ((2.1)*1.02), img_blur, ((-1.4)*1.02), 0)


cv2.imwrite('enhanced_image.jpg', img_usm)
