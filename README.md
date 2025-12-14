# Template Matching with OpenCV

This project demonstrates template matching using OpenCV and a manual implementation of the Normalized Cross-Correlation (NCC) algorithm.

---

## 🇹🇷 Proje Açıklaması (Türkçe)

Bu projede OpenCV kütüphanesi kullanılarak Template Matching yöntemi uygulanmıştır. Ayrıca aynı algoritma, Normalized Cross-Correlation (NCC) yöntemi temel alınarak manuel olarak implemente edilmiştir. Elde edilen sonuçlar görsel ve sayısal olarak karşılaştırılmıştır.

---

## Project Objective

- Apply OpenCV's built-in template matching method
- Implement the same algorithm from scratch
- Compare the results visually and numerically

---

## Technologies

- Python 3.10
- OpenCV
- NumPy
- Matplotlib

---

## Project Structure
```text
TemplateMatchingProject/
├── images/
│   ├── source.jpg
│   └── template.jpg
├── main.py
├── opencv_tm.py
├── manual_tm.py
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install required dependencies

The required Python libraries are listed in the `requirements.txt` file. Install them using the following command:
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python main.py
```

---

## Features

- **OpenCV Template Matching**: Uses OpenCV's `cv2.matchTemplate()` function with NCC method
- **Manual NCC Implementation**: Custom implementation of Normalized Cross-Correlation algorithm
- **Visual Comparison**: Side-by-side visualization of results from both methods
- **Numerical Analysis**: Comparison of correlation scores and execution times

---

## Output

The program will display:
- Original source image with detected template locations
- Comparison between OpenCV and manual implementation results
- Performance metrics and accuracy measurements

---

## Requirements

See `requirements.txt` for the complete list of dependencies:
- opencv-python
- numpy
- matplotlib

---

## License

This project is open source and available for educational purposes.

---

## Author

Template Matching Implementation Project