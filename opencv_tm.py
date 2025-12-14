import cv2

def opencv_template_matching(source_path, template_path):
    source = cv2.imread(source_path, 0)
    template = cv2.imread(template_path, 0)

    h, w = template.shape

    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    source_color = cv2.imread(source_path)
    cv2.rectangle(source_color, top_left, bottom_right, (0, 0, 255), 2)

    return source_color, max_val
