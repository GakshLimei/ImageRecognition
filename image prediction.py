from PIL import Image
from ultralytics import YOLO

# 加载预训练的YOLOv8n模型
model = YOLO('./yolo v8 models/yolov8n.pt')

# 在指定的图片上运行推理
results = model('test_images/image7.jpg')  # 结果列表

# 展示结果
for r in results:
    im_array = r.plot()  # 绘制包含预测结果的BGR numpy数组
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL图像
    im.show()  # 显示图像
    im.save('results.jpg')  # 保存图像