import cv2
import numpy as np
import easyocr
import imutils

def getCarNumber(image_path):
    img = cv2.imread(image_path)
    img_blur = cv2.GaussianBlur(img, (7, 7), 1)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
    # plt.imshow(cv2.cvtColor(img_gray,cv2.COLOR_BGR2RGB))

    bfilter = cv2.bilateralFilter(img_gray, 11, 17, 17)
    edge = cv2.Canny(bfilter, 30, 200)
    kernel = np.zeros((5, 5), np.uint8)
    img_dilation = cv2.dilate(edge, kernel, iterations=1)
    # plt.imshow(cv2.cvtColor(img_dilation,cv2.COLOR_GRAY2RGB))

    img_copy = img_dilation.copy()
    contours = cv2.findContours(
        img_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    keypoints = imutils.grab_contours(contours)
    contours = sorted(keypoints, key=cv2.contourArea, reverse=True)[:10]
    # print(contours)
    # plt.imshow(cv2.cvtColor(img_copy,cv2.COLOR_BGR2RGB))

    plateLocation = None
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 10, True)
        if (len(approx) == 4):
            plateLocation = approx
            break

    mask = np.zeros(img_gray.shape, np.uint8)
    numberPlate = cv2.drawContours(mask, [plateLocation], 0, 255, -1)
    numberPlate = cv2.bitwise_and(img, img, mask=mask)

    # plt.imshow(cv2.cvtColor(numberPlate,cv2.COLOR_BGR2RGB))

    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    croppedImage = img_gray[x1:x2+1, y1:y2+1]
    # plt.imshow(cv2.cvtColor(croppedImage,cv2.COLOR_BGR2RGB))

    reader = easyocr.Reader(['en'])
    result = reader.readtext(croppedImage)
    return result[-1][-2]
