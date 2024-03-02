from ultralytics.utils.benchmarks import benchmark

# 在GPU上进行基准测试
benchmark(model='./yolo v8 models/yolov8n.pt', data='coco8.yaml', imgsz=640, half=False, device=0)