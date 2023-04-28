import cv2

# Get the image number from user input
n = input("Enter the image number:")

# Load the image in grayscale
img = cv2.imread(n + '.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to the image
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Apply the unsharp mask to the image
img_usm = cv2.addWeighted(img, ((2.1)*1.02), img_blur, ((-1.4)*1.02), 0)

# Save the enhanced image
cv2.imwrite('enhanced_image.jpg', img_usm)
