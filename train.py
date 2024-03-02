from ultralytics import YOLO

# 加载一个模型
model = YOLO('yolov8n.yaml')  # 从YAML建立一个新模型
model = YOLO('yolo v8 models/yolov8n.ptyolov8n.pt')  # 加载预训练模型（推荐用于训练）
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # 从YAML建立并转移权重

# 训练模型
if __name__ == '__main__':
    results = model.train(data='coco128.yaml', epochs=100, imgsz=640)