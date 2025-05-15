# YOLOv5 Object Detector

A simple web app for real-time object detection and explanation using the pre-trained YOLOv5 model.
---

## Overview

This app uses the **YOLOv5s** model pre-trained on the **COCO dataset** (80 object classes) for detecting objects in user-uploaded images. The model is loaded directly from the [Ultralytics GitHub repository](https://github.com/ultralytics/yolov5) via `torch.hub`.

---

## 📦 Tech Stack

- **YOLOv5** – Pre-trained model for object detection (Ultralytics)
- **COCO Dataset** – 80 common object classes (e.g., person, car, dog)
- **Gradio** – Web interface for interaction
- **Hugging Face Spaces** – Free cloud deployment
- **PyTorch** – For deep learning inference
- **Pandas** – For processing prediction results

---

## ✅ Features

- Upload an image to detect objects instantly
- Displays object names and count
- Explains what’s in the image using natural language
- Informs the user if no recognizable objects are found
- Works directly with a pre-trained model — no need to download or train anything

---

## 🚀 How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/object-detection-app.git
cd object-detection-app
