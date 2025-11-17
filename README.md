# 🚗 Car Detection - Real-time Vehicle Detection and Classification System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-Detection-green.svg)](https://github.com/ultralytics/yolov5)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Real-time vehicle detection and classification system using deep learning. Detects and classifies vehicles in images and video streams with high accuracy.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Applications](#applications)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Real-time Detection**: Detect vehicles in real-time from video streams or webcam
- **Image Processing**: Process single images or image batches
- **Multi-vehicle Tracking**: Track multiple vehicles simultaneously
- **Vehicle Classification**: Classify different types of vehicles
- **Vehicle Counting**: Count vehicles in traffic scenes
- **Annotation Tools**: Built-in tools for dataset annotation
- **High Accuracy**: Powered by YOLO/Faster R-CNN deep learning models

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended for faster processing)
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/talha-eren/Car_Deteticon.git
cd Car_Deteticon
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Download Model Weights

The trained model weights are located at `Car_Detection/best.pt`. Make sure this file exists in the project directory.

## 💻 Usage

### Basic Image Detection

```bash
python detect.py --source path/to/image.jpg
```

### Video Detection

```bash
python detect.py --source path/to/video.mp4
```

### Webcam Detection

```bash
python detect.py --source 0
```

### Custom Options

```bash
python detect.py \
    --source path/to/input \
    --weights Car_Detection/best.pt \
    --conf 0.25 \
    --save-txt \
    --save-conf
```

### Parameters

- `--source`: Input source (image, video, webcam, or directory)
- `--weights`: Path to model weights (default: `Car_Detection/best.pt`)
- `--conf`: Confidence threshold (default: 0.25)
- `--save-txt`: Save results as text files
- `--save-conf`: Save confidence scores
- `--img-size`: Image size for inference (default: 640)

## 📁 Project Structure

```
Car_Deteticon/
│
├── Car_Detection/
│   ├── best.pt              # Trained model weights
│   ├── runs/
│   │   └── detect/          # Detection results output
│   │       └── ...
│   └── ...
│
├── detect.py                # Main detection script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore               # Git ignore file
```

## 🎯 Model Information

- **Model Type**: YOLO (You Only Look Once)
- **Model File**: `Car_Detection/best.pt`
- **Input Size**: 640x640 pixels (configurable)
- **Output**: Bounding boxes with class labels and confidence scores

### Viewing Results

Detection results are saved in `Car_Detection/runs/detect/` directory. Each run creates a new folder with timestamp.

## 🔧 Applications

### Traffic Analysis
- Monitor traffic flow in real-time
- Analyze vehicle density at intersections
- Generate traffic statistics

### Parking Management
- Detect available parking spaces
- Monitor parking lot occupancy
- Track vehicle entry/exit

### Surveillance Systems
- Security monitoring
- Vehicle tracking
- Anomaly detection

### Research & Development
- Dataset creation and annotation
- Model training and evaluation
- Computer vision research

## 🛠️ Development

### Training Custom Model

To train your own model:

```bash
python train.py \
    --data dataset.yaml \
    --epochs 100 \
    --batch-size 16 \
    --img-size 640
```

### Dataset Format

The model expects datasets in YOLO format:
- Images in `images/` folder
- Annotations in `labels/` folder (YOLO format: class x y w h)

## 📊 Performance

- **Inference Speed**: ~30-60 FPS (GPU), ~5-10 FPS (CPU)
- **Accuracy**: mAP@0.5 > 0.85 (depending on dataset)
- **Model Size**: ~50-100 MB

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Talha Eren**

- GitHub: [@talha-eren](https://github.com/talha-eren)



# 🚗 Araç Tespiti - Gerçek Zamanlı Araç Tespit ve Sınıflandırma Sistemi

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![YOLO](https://img.shields.io/badge/YOLO-Tespit-green.svg)](https://github.com/ultralytics/yolov5)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Derin öğrenme kullanarak gerçek zamanlı araç tespit ve sınıflandırma sistemi. Görüntüler ve video akışlarında araçları yüksek doğrulukla tespit eder ve sınıflandırır.

## 📋 İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Model Bilgileri](#model-bilgileri)
- [Uygulama Alanları](#uygulama-alanları)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## ✨ Özellikler

- **Gerçek Zamanlı Tespit**: Video akışlarından veya webcam'den gerçek zamanlı araç tespiti
- **Görüntü İşleme**: Tek görüntü veya görüntü gruplarını işleme
- **Çoklu Araç Takibi**: Aynı anda birden fazla aracı takip etme
- **Araç Sınıflandırma**: Farklı araç türlerini sınıflandırma
- **Araç Sayma**: Trafik sahnelerinde araç sayma
- **Açıklama Araçları**: Veri seti açıklama için yerleşik araçlar
- **Yüksek Doğruluk**: YOLO/Faster R-CNN derin öğrenme modelleri ile güçlendirilmiş

## 🚀 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- CUDA destekli GPU (daha hızlı işleme için önerilir)
- pip paket yöneticisi

### Adım 1: Depoyu Klonlayın

```bash
git clone https://github.com/talha-eren/Car_Deteticon.git
cd Car_Deteticon
```

### Adım 2: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 3: Model Ağırlıklarını İndirin

Eğitilmiş model ağırlıkları `Car_Detection/best.pt` konumunda bulunmaktadır. Bu dosyanın proje dizininde mevcut olduğundan emin olun.

## 💻 Kullanım

### Temel Görüntü Tespiti

```bash
python detect.py --source path/to/image.jpg
```

### Video Tespiti

```bash
python detect.py --source path/to/video.mp4
```

### Webcam Tespiti

```bash
python detect.py --source 0
```

### Özel Seçenekler

```bash
python detect.py \
    --source path/to/input \
    --weights Car_Detection/best.pt \
    --conf 0.25 \
    --save-txt \
    --save-conf
```

### Parametreler

- `--source`: Giriş kaynağı (görüntü, video, webcam veya dizin)
- `--weights`: Model ağırlıkları yolu (varsayılan: `Car_Detection/best.pt`)
- `--conf`: Güven eşiği (varsayılan: 0.25)
- `--save-txt`: Sonuçları metin dosyaları olarak kaydet
- `--save-conf`: Güven skorlarını kaydet
- `--img-size`: Çıkarım için görüntü boyutu (varsayılan: 640)

## 📁 Proje Yapısı

```
Car_Deteticon/
│
├── Car_Detection/
│   ├── best.pt              # Eğitilmiş model ağırlıkları
│   ├── runs/
│   │   └── detect/          # Tespit sonuçları çıktısı
│   │       └── ...
│   └── ...
│
├── detect.py                # Ana tespit scripti
├── requirements.txt          # Python bağımlılıkları
├── README.md                 # Proje dokümantasyonu
└── .gitignore               # Git ignore dosyası
```

## 🎯 Model Bilgileri

- **Model Türü**: YOLO (You Only Look Once)
- **Model Dosyası**: `Car_Detection/best.pt`
- **Giriş Boyutu**: 640x640 piksel (yapılandırılabilir)
- **Çıktı**: Sınıf etiketleri ve güven skorları ile sınırlayıcı kutular

### Sonuçları Görüntüleme

Tespit sonuçları `Car_Detection/runs/detect/` dizininde kaydedilir. Her çalıştırma zaman damgası ile yeni bir klasör oluşturur.

## 🔧 Uygulama Alanları

### Trafik Analizi
- Trafik akışını gerçek zamanlı izleme
- Kavşaklardaki araç yoğunluğunu analiz etme
- Trafik istatistikleri oluşturma

### Otopark Yönetimi
- Boş park yerlerini tespit etme
- Otopark doluluk oranını izleme
- Araç giriş/çıkış takibi

### Güvenlik Sistemleri
- Güvenlik izleme
- Araç takibi
- Anomali tespiti

### Araştırma ve Geliştirme
- Veri seti oluşturma ve açıklama
- Model eğitimi ve değerlendirme
- Bilgisayarlı görü araştırmaları

## 🛠️ Geliştirme

### Özel Model Eğitimi

Kendi modelinizi eğitmek için:

```bash
python train.py \
    --data dataset.yaml \
    --epochs 100 \
    --batch-size 16 \
    --img-size 640
```

### Veri Seti Formatı

Model YOLO formatında veri setleri bekler:
- Görüntüler `images/` klasöründe
- Açıklamalar `labels/` klasöründe (YOLO formatı: class x y w h)

## 📊 Performans

- **Çıkarım Hızı**: ~30-60 FPS (GPU), ~5-10 FPS (CPU)
- **Doğruluk**: mAP@0.5 > 0.85 (veri setine bağlı)
- **Model Boyutu**: ~50-100 MB

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir Pull Request göndermekten çekinmeyin.

1. Depoyu fork edin
2. Özellik dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dalınıza push yapın (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

## 👤 Yazar

**Talha Eren**

- GitHub: [@talha-eren](https://github.com/talha-eren)




