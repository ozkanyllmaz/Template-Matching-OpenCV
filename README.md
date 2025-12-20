# Şablon Eşleştirme (Template Matching) Projesi

Bu proje, OpenCV kütüphanesi kullanarak ve manuel algoritma implementasyonu yaparak şablon eşleştirme yöntemini uygular. Büyük bir görüntü içinde küçük bir şablon görüntüyü arar ve konumunu tespit eder.

---

## 📋 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
- [Proje Yapısı](#proje-yapısı)
- [Metotlar ve İşlevleri](#metotlar-ve-i̇şlevleri)
- [Algoritma Açıklaması](#algoritma-açıklaması)
- [Sonuçlar](#sonuçlar)

---

## 🎯 Proje Hakkında

### Amaç
Bu projede iki farklı yaklaşımla şablon eşleştirme gerçekleştirilmiştir:
1. **OpenCV'nin Hazır Fonksiyonu**: `cv2.matchTemplate()` kullanılarak
2. **Manuel Implementasyon**: Normalleştirilmiş Çapraz Korelasyon (NCC - Normalized Cross-Correlation) algoritması sıfırdan kodlanarak

### Ne Yapar?
Program, kaynak görüntü içinde şablon görüntünün en iyi eşleşen konumunu bulur ve yeşil dikdörtgen ile işaretler. Her iki yöntemin sonuçları görsel ve sayısal olarak karşılaştırılır.

---

## 🛠 Kullanılan Teknolojiler

- **Python 3.10+**: Programlama dili
- **OpenCV (cv2)**: Görüntü işleme ve bilgisayarlı görü kütüphanesi
- **NumPy**: Sayısal hesaplamalar ve matris işlemleri için
- **Matplotlib**: Sonuçların görselleştirilmesi için

---

## 🚀 Kurulum ve Çalıştırma

### 1. Sanal Ortam Oluşturma (Önerilen)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 2. Gerekli Kütüphaneleri Yükleme
```bash
pip install -r requirements.txt
```

### 3. Projeyi Çalıştırma
```bash
python main.py
```

---

## 📁 Proje Yapısı

```
TemplateMatchingProject/
├── images/                  # Görüntü dosyaları klasörü
│   ├── source.jpg          # Ana (kaynak) görüntü
│   └── template.jpg        # Aranacak şablon görüntü
├── main.py                 # Ana program dosyası
├── opencv_tm.py            # OpenCV şablon eşleştirme modülü
├── manual_tm.py            # Manuel NCC implementasyon modülü
├── requirements.txt        # Gerekli Python kütüphaneleri
└── README.md              # Proje dokümantasyonu
```

---

## 🔧 Metotlar ve İşlevleri

### 1. `opencv_template_matching(source_path, template_path)`

**Dosya**: `opencv_tm.py`

**Amaç**: OpenCV'nin hazır fonksiyonunu kullanarak şablon eşleştirme yapar.

**Parametreler**:
- `source_path` (str): Kaynak görüntünün dosya yolu
- `template_path` (str): Şablon görüntünün dosya yolu

**Dönüş Değeri**:
- `result_image` (numpy.ndarray): Eşleşme konumu işaretlenmiş renkli görüntü
- `max_score` (float): En yüksek benzerlik skoru (0-1 arası)
- `max_location` (tuple): En iyi eşleşmenin koordinatları (x, y)

**Çalışma Prensibi**:
```python
# 1. Görüntüleri yükle
source = cv2.imread(source_path, 0)  # Gri tonlamalı
template = cv2.imread(template_path, 0)

# 2. OpenCV matchTemplate fonksiyonunu kullan
result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)

# 3. En yüksek korelasyon değerini bul
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 4. Bulunan konumu işaretle
cv2.rectangle(source_color, max_loc, (max_loc[0] + tw, max_loc[1] + th), (0, 255, 0), 5)
```

**Kullanılan Yöntem**: `cv2.TM_CCOEFF_NORMED` - Normalleştirilmiş korelasyon katsayısı

---

### 2. `manual_template_matching(source_path, template_path)`

**Dosya**: `manual_tm.py`

**Amaç**: NCC algoritmasını sıfırdan kodlayarak şablon eşleştirme yapar.

**Parametreler**:
- `source_path` (str): Kaynak görüntünün dosya yolu
- `template_path` (str): Şablon görüntünün dosya yolu

**Dönüş Değeri**:
- `result_image` (numpy.ndarray): Eşleşme konumu işaretlenmiş renkli görüntü
- `best_score` (float): En yüksek benzerlik skoru (0-1 arası)

**Çalışma Adımları**:

#### 2.1. Görüntü Yükleme ve Boyut Alma
```python
source = cv2.imread(source_path, 0)  # Kaynak görüntüyü gri tonlamalı yükle
template = cv2.imread(template_path, 0)  # Şablon görüntüyü gri tonlamalı yükle

sh, sw = source.shape  # Kaynak görüntü yükseklik ve genişlik
th, tw = template.shape  # Şablon görüntü yükseklik ve genişlik
```

#### 2.2. Şablon İstatistiklerinin Hesaplanması
```python
t_mean = np.mean(template)  # Şablonun ortalama piksel değeri
t_std = np.std(template)  # Şablonun standart sapması
```

**Neden Gerekli?**: NCC algoritması, görüntü parlaklığından bağımsız çalışmak için normalleştirilmiş değerler kullanır.

#### 2.3. Kayıcı Pencere (Sliding Window) ile Tarama
```python
for y in range(sh - th):  # Dikey tarama
    for x in range(sw - tw):  # Yatay tarama
        window = source[y:y+th, x:x+tw]  # Pencere al
```

**Açıklama**: Kaynak görüntü üzerinde şablon boyutunda bir pencere kaydırılır. Her konumda benzerlik hesaplanır.

#### 2.4. Normalleştirilmiş Çapraz Korelasyon Hesaplama
```python
w_mean = np.mean(window)  # Pencerenin ortalama değeri
w_std = np.std(window)  # Pencerenin standart sapması

# Sıfıra bölme hatası kontrolü
if w_std == 0:
    continue

# NCC formülü
score = np.sum((window - w_mean) * (template - t_mean))
score /= (w_std * t_std * th * tw)
```

**Matematiksel Formül**:
```
NCC = Σ[(W - W̄) × (T - T̄)] / (σw × σt × N)

W: Pencere pikselleri
T: Şablon pikselleri
W̄: Pencere ortalaması
T̄: Şablon ortalaması
σw: Pencere standart sapması
σt: Şablon standart sapması
N: Toplam piksel sayısı
```

**Skor Değerleri**:
- `1.0`: Mükemmel eşleşme
- `0.0`: Hiç benzerlik yok
- `-1.0`: Ters eşleşme (negatif korelasyon)

#### 2.5. En İyi Eşleşmeyi Bulma
```python
if score > best_score:
    best_score = score
    best_loc = (x, y)  # En iyi konumu kaydet
```

#### 2.6. Sonucu Görselleştirme
```python
source_color = cv2.imread(source_path)  # Renkli yükle
cv2.rectangle(
    source_color,
    best_loc,  # Sol üst köşe
    (best_loc[0] + tw, best_loc[1] + th),  # Sağ alt köşe
    (0, 255, 0),  # Yeşil renk (BGR formatı)
    5  # Çizgi kalınlığı
)
```

---

### 3. `main.py` - Ana Program

**İşlevler**:

#### 3.1. Görüntüleri Yükleme ve Gösterme
```python
source_image = cv2.imread('images/source.jpg')
template_image = cv2.imread('images/template.jpg')
```

#### 3.2. Her İki Yöntemi Çalıştırma
```python
# OpenCV yöntemi
opencv_result, opencv_score, opencv_loc = opencv_template_matching(source_path, template_path)

# Manuel yöntem
manual_result, manual_score = manual_template_matching(source_path, template_path)
```

#### 3.3. Performans Karşılaştırması
```python
import time

# Çalışma sürelerini ölç
start = time.time()
opencv_result, opencv_score, opencv_loc = opencv_template_matching(...)
opencv_time = time.time() - start

start = time.time()
manual_result, manual_score = manual_template_matching(...)
manual_time = time.time() - start
```

#### 3.4. Sonuçları Görselleştirme
```python
# Matplotlib ile yan yana göster
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(cv2.cvtColor(opencv_result, cv2.COLOR_BGR2RGB))
axes[0].set_title(f'OpenCV - Skor: {opencv_score:.4f}')
axes[1].imshow(cv2.cvtColor(manual_result, cv2.COLOR_BGR2RGB))
axes[1].set_title(f'Manuel - Skor: {manual_score:.4f}')
plt.show()
```

---

## 📊 Algoritma Açıklaması

### Normalleştirilmiş Çapraz Korelasyon (NCC) Nedir?

NCC, iki görüntü parçasının benzerliğini ölçen istatistiksel bir yöntemdir.

**Avantajları**:
- ✅ Işık değişimlerinden etkilenmez (normalleştirilmiş)
- ✅ Parlaklık farklılıklarına karşı dayanıklı
- ✅ -1 ile 1 arasında standart çıktı verir

**Çalışma Mantığı**:
1. Her piksel için ortalamadan farkı alınır
2. Bu farklar çarpılır ve toplanır
3. Standart sapmalara bölünerek normalleştirilir
4. Sonuç -1 ile 1 arasında bir benzerlik skorudur

### Manuel ve OpenCV Yöntemleri Arasındaki Farklar

| Özellik | Manuel NCC | OpenCV |
|---------|-----------|---------|
| **Hız** | Yavaş (Python döngüleri) | Çok hızlı (C++ optimizasyonu) |
| **Doğruluk** | Yüksek | Yüksek |
| **Esneklik** | Kod üzerinde tam kontrol | Hazır fonksiyon |
| **Öğretici Değer** | Yüksek (algoritma anlaşılır) | Düşük (kara kutu) |

---

## 📈 Sonuçlar

### OpenCV Şablon Eşleştirme Sonucu
![OpenCV Template Matching Result](https://github.com/user-attachments/assets/1ed44e3f-f08a-4b94-bd44-14146ef475b4)

**Özellikler**:
- Çalışma süresi: ~0.01-0.05 saniye
- Benzerlik skoru: 0.95-1.0
- Doğruluk: Çok yüksek

### Manuel NCC Implementasyonu Sonucu
![Manual NCC Implementation Result](https://github.com/user-attachments/assets/7c35055c-b9de-4057-93ab-bb08e0941f4c)

**Özellikler**:
- Çalışma süresi: ~2-10 saniye (görüntü boyutuna bağlı)
- Benzerlik skoru: OpenCV ile neredeyse aynı
- Doğruluk: Çok yüksek

### Karşılaştırma
- ✅ Her iki yöntem de aynı konumu bulur
- ✅ Skor değerleri birbirine çok yakındır
- ⚠️ OpenCV, manuel yöntemden 100-1000x daha hızlıdır
- 📚 Manuel yöntem, algoritmanın nasıl çalıştığını anlamak için idealdir

---

## 📦 Gereksinimler

`requirements.txt` dosyasında listelenen kütüphaneler:
```
opencv-python>=4.5.0
numpy>=1.21.0
matplotlib>=3.4.0
```

---

## 🎓 Eğitim Amaçlı Kullanım

Bu proje, aşağıdaki konuları öğrenmek için idealdir:
- Görüntü işleme temelleri
- Şablon eşleştirme algoritmaları
- NumPy ile matris işlemleri
- OpenCV kütüphanesi kullanımı
- Algoritma performans karşılaştırması

---

## 📝 Lisans

Bu proje eğitim amaçlı hazırlanmıştır ve açık kaynak kodludur.

---
