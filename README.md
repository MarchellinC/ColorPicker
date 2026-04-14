# 🎨 Color Picker App (Dominant Color Extractor)

## 📌 Deskripsi
Color Picker App adalah aplikasi berbasis **Streamlit** yang memungkinkan pengguna:
- Mengupload gambar
- Mengekstrak warna dominan dari gambar
- Menampilkan hasil warna dalam format HEX

Aplikasi ini menggunakan **Machine Learning (KMeans Clustering)** untuk mengidentifikasi warna utama dari gambar.

---

## 🚀 Fitur Utama

- 🖼️ Upload gambar (JPG/PNG)
- 🎯 Ekstraksi 5 warna dominan otomatis
- 🎨 Tampilan warna dalam bentuk swatch
- 🌈 Background UI dinamis mengikuti warna gambar
- 🔢 Output kode warna HEX

---

## 🧠 Teknologi yang Digunakan

- Python
- Streamlit
- NumPy
- Scikit-learn (KMeans)
- Pillow (PIL)

---

## ⚙️ Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

---

## 🔍 Cara Kerja

1. User upload gambar
2. Gambar diproses dan di-resize
3. Pixel diubah menjadi array RGB
4. KMeans clustering digunakan untuk menemukan warna dominan
5. Hasil ditampilkan dalam:
   - Swatch warna
   - Kode HEX
   - Background dinamis

---

## 📊 Machine Learning

- Algoritma: KMeans Clustering
- Input: Pixel RGB
- Output: Cluster warna dominan

---

## 🌟 Keunggulan

- UI modern dan responsif
- Background adaptif berdasarkan warna gambar
- Cepat dan ringan
- Cocok untuk desain, branding, dan analisis warna

---

## 🚧 Future Improvement

- Export palette ke file
- Copy HEX dengan klik
- Support lebih banyak warna
- Integrasi dengan tools design

---

## 👨‍💻 Author
Marchellin Chenika

---

## ⭐ Support
Jika project ini membantu:
- ⭐ Star repo
- 🍴 Fork repo
- 📢 Share ke LinkedIn
