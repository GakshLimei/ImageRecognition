from ultralytics import YOLO

# 加载模型
model = YOLO('yolo v8 models/yolov8n.pt')  # 加载官方模型
model = YOLO('runs/detect/train3/weights/best.pt')  # 加载自定义训练的模型

# 导出模型
model.export(format='onnx')