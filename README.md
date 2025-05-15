# YOLOv5 Object Detector

A simple web app for real-time object detection and explanation using the pre-trained YOLOv5 model.

---

## Project Structure

object-detection-app/
│
├── app.py # Main application code
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## Overview

This app uses the **YOLOv5s** model pre-trained on the **COCO dataset** (80 object classes) for detecting objects in user-uploaded images. The model is loaded directly from the [Ultralytics GitHub repository](https://github.com/ultralytics/yolov5) via `torch.hub`.

---

## Workflow

```mermaid
flowchart TD
    A[User Uploads Image] --> B[Image Processed by YOLOv5 Model]
    B --> C{Objects Detected?}
    C -- Yes --> D[Display Detected Objects and Counts]
    C -- No --> E[Show "No objects found" Message]

### How to run locally 

git clone https://github.com/your-username/object-detection-app.git
cd object-detection-app
pip install -r requirements.txt
python app.py
