import cv2
from opencv_tm import opencv_template_matching
from manual_tm import manual_template_matching

source = "images/source1.jpg"
template = "images/template1.jpg"

opencv_img, opencv_score = opencv_template_matching(source, template)
manual_img, manual_score = manual_template_matching(source, template)

print("OpenCV Score:", opencv_score)
print("Manual Score:", manual_score)

cv2.imshow("OpenCV Result", opencv_img)
cv2.imshow("Manual Result", manual_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
