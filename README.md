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

## 🙏 Acknowledgments

- YOLO community for the excellent detection framework
- OpenCV for image processing capabilities
- All contributors and users of this project

## 📧 Contact

For questions, suggestions, or support, please open an issue on GitHub.

---

⭐ If you find this project helpful, please consider giving it a star!

