# app.py

import torch
from PIL import Image
import gradio as gr

# Load YOLOv5 pretrained on COCO
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Object detection function with explanation
def detect_and_explain(img):
    results = model(img)
    labels = results.pandas().xyxy[0]['name'].tolist()

    if len(labels) == 0:
        return "❌ No objects detected. This image may contain uncommon elements not included in the COCO dataset (e.g., abstract art, rare animals, unusual scenes)."

    label_counts = {}
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1

    explanation = f"✅ Detected {len(labels)} object(s):\n"
    for label, count in label_counts.items():
        explanation += f"🔹 {label}: {count} time(s)\n"

    return explanation

# Launch Gradio interface
gr.Interface(
    fn=detect_and_explain,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(),
    title="Smart Image Object Detector",
    description="Upload an image. The app detects and explains what's in it using YOLOv5 pretrained on the COCO dataset."
).launch()
