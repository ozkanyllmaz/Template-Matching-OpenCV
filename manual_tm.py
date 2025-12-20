import cv2
import numpy as np

def manual_template_matching(source_path, template_path):
    source = cv2.imread(source_path, 0) 
    template = cv2.imread(template_path, 0)

    sh, sw = source.shape   # sh = ana resmin yüksekliği, sw = ana resmin genişliği
    th, tw = template.shape    # th = şablon yüksekliği, tw = şablon genişliği

    t_mean = np.mean(template)
    t_std = np.std(template)

    best_score = -1
    best_loc = (0, 0)

    for y in range(sh - th):    # Ana resimde yukarıdan aşağıya tara
        for x in range(sw - tw):    # Soldan sağa tara
            window = source[y:y+th, x:x+tw]    # Şablon boyutunda bir pencere al

            #Benzerlik Skoru Hesaplama
            w_mean = np.mean(window)    # Pencerenin ortalama parlaklığı
            w_std = np.std(window)  # Pencerenin standart sapması

            if w_std == 0:
                continue

            # Korelasyon katsayısı hesaplama (ne kadar benzer?)
            score = np.sum((window - w_mean) * (template - t_mean))
            score /= (w_std * t_std * th * tw)

            if score > best_score:
                best_score = score
                best_loc = (x, y)

    source_color = cv2.imread(source_path)
    cv2.rectangle(
        source_color,
        best_loc,   # Dikdörtgenin sol üst köşesi
        (best_loc[0] + tw, best_loc[1] + th),   # Sağ alt köşe
        (0, 255, 0),    # Yeşil renk (BGR formatında)
        5  # Çizgi kalınlığı
    )

    return source_color, best_score
