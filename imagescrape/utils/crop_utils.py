import os
import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path

from ultralytics import YOLO
import cv2
import os
import numpy as np
from pathlib import Path

def crop_with_yolo_or_face(image_paths, cropped_dir="cropped", pfp_size=512, model_path="C:\\Users\\shrey\\Downloads\\best.pt"
):
    os.makedirs(cropped_dir, exist_ok=True)
    model = YOLO(model_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cropped_paths = []

    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is None:
            continue
        h, w = img.shape[:2]

        # Run YOLOv11 inference
        results = model(img)[0]
        boxes = results.boxes.xyxy.cpu().numpy().astype(int)

        if len(boxes) > 0:
            x1, y1, x2, y2 = boxes[0]
        else:
            # Fallback: OpenCV face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 0:
                continue
            x1, y1, fw, fh = faces[0]
            x2, y2 = x1 + fw, y1 + fh

        # Expand crop region
        box_w, box_h = x2 - x1, y2 - y1
        pad_w, pad_h = int(box_w * 0.4), int(box_h * 0.6)
        x1 = max(0, x1 - pad_w)
        y1 = max(0, y1 - pad_h)
        x2 = min(w, x2 + pad_w)
        y2 = min(h, y2 + pad_h)

        cropped = img[y1:y2, x1:x2]
        if cropped.size == 0:
            continue

        # Center crop to square and resize
        ch, cw = cropped.shape[:2]
        size = max(ch, cw)
        square = 255 * np.ones((size, size, 3), dtype=np.uint8)
        y_offset = (size - ch) // 2
        x_offset = (size - cw) // 2
        square[y_offset:y_offset + ch, x_offset:x_offset + cw] = cropped
        resized = cv2.resize(square, (pfp_size, pfp_size))

        out_path = f"{cropped_dir}/{Path(img_path).stem}_pfp.jpg"
        cv2.imwrite(out_path, resized)
        cropped_paths.append(out_path)

    return cropped_paths

