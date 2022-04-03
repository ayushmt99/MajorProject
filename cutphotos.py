import cv2
import os
path_to_image="./Photos/together.png"
image= cv2.imread(path_to_image)
(h,w) = image.shape[:2]
centerX, centerY = (w//2), (h//2)
topLeft = image[0:centerY, 0:centerX]
topRight = image[0:centerY, centerX:w]
bottomLeft=image[centerY:h,0:centerX]
bottomRight = image[centerY:h , centerX:w]

cv2.imshow("topLeft" , topLeft)
cv2.imshow("topRight" , topRight)
cv2.imshow("bottomLeft" , bottomLeft)
cv2.imshow("bottomRight" , bottomRight)
path =r"./upload_images"
isWritten= cv2.imwrite(os.path.join(path , 'waka1.jpg'), topLeft)
isWritten= cv2.imwrite(os.path.join(path , 'waka2.jpg'), topRight)
isWritten= cv2.imwrite(os.path.join(path , 'waka3.jpg'), bottomLeft)
isWritten= cv2.imwrite(os.path.join(path , 'waka4.jpg'), bottomRight)
if isWritten:
    print('Image is successfully saved as file.')
cv2.waitKey(0)



