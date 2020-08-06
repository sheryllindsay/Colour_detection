import color_detector_mark3 as cd
#import color_detector_final as cd
import cv2


img =cv2.imread("dog.jpg")
color=cd.getColorName(img,500,100)
print(color)
