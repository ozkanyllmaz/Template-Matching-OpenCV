import cv2
import numpy as np

def manual_template_matching(source_path, template_path):
    source = cv2.imread(source_path, 0)
    template = cv2.imread(template_path, 0)

    sh, sw = source.shape
    th, tw = template.shape

    t_mean = np.mean(template)
    t_std = np.std(template)

    best_score = -1
    best_loc = (0, 0)

    for y in range(sh - th):
        for x in range(sw - tw):
            window = source[y:y+th, x:x+tw]

            w_mean = np.mean(window)
            w_std = np.std(window)

            if w_std == 0:
                continue

            score = np.sum((window - w_mean) * (template - t_mean))
            score /= (w_std * t_std * th * tw)

            if score > best_score:
                best_score = score
                best_loc = (x, y)

    source_color = cv2.imread(source_path)
    cv2.rectangle(
        source_color,
        best_loc,
        (best_loc[0] + tw, best_loc[1] + th),
        (0, 255, 0),
        2
    )

    return source_color, best_score
