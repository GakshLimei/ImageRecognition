import cv2
from ultralytics import YOLO

# 加载YOLOv8模型
model = YOLO('../yolo v8/yolov8n.pt')

# 使用默认摄像头
video_path = 0
cap = cv2.VideoCapture(video_path)

# 设置摄像头的分辨率
desired_width = 1280
desired_height = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

# 定义帧的步长
frame_step = 2  # 每隔2帧处理一帧

# 初始化计数器
frame_count = 0

# 遍历视频帧
while cap.isOpened():
    # 从摄像头中读取一帧
    success, frame = cap.read()

    if success:
        # 如果计数器等于帧的步长，则进行YOLOv8推理
        if frame_count == 0:
            # 在该帧上运行YOLOv8推理
            results = model(frame)

            # 在帧上可视化结果
            annotated_frame = results[0].plot()

            # 显示带注释的帧
            cv2.imshow("YOLOv8 inference", annotated_frame)

        # 更新计数器
        frame_count = (frame_count + 1) % frame_step

        # 如果按下'q'则中断循环
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # 如果摄像头关闭则中断循环
        break

# 释放摄像头捕获对象并关闭显示窗口
cap.release()
cv2.destroyAllWindows()