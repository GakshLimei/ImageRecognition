import cv2
from ultralytics import YOLO
import time

# 加载YOLOv8模型
model = YOLO('../yolo v8 models/yolov8n.pt')

# 打开视频文件
video_path = "D:\\Users\\Admin\\Videos\\Captures\\(27) #AFCCup - Full Match - Group F _ Phnom Penh Crown FC (CAM) vs Dynamic Herb Cebu FC (PHI) - YouTube.mp4"
cap = cv2.VideoCapture(video_path)

# 设置视频分辨率
desired_width = 1280
desired_height = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

# 初始化变量
prev_frame_time = 0
new_frame_time = 0

# 遍历视频帧
while cap.isOpened():
    # 从视频中读取一帧
    success, frame = cap.read()

    if success:
        # 记录开始时间
        start_time = time.time()

        # 在该帧上运行YOLOv8推理
        results = model(frame)

        # 在帧上可视化结果
        annotated_frame = results[0].plot()

        # 记录结束时间
        end_time = time.time()

        # 计算推理时间
        inference_time = (end_time - start_time) * 1000  # 转换为毫秒

        # 计算帧率
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time

        # 将帧率和推理时间添加到帧上
        fps_text = f"FPS: {int(fps)} | {inference_time:.2f} ms"
        cv2.putText(annotated_frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # 显示带注释的帧
        cv2.imshow("YOLOv8 inference", annotated_frame)

        # 如果按下'q'则中断循环
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # 如果视频结束则中断循环
        break

# 释放视频捕获对象并关闭显示窗口
cap.release()
cv2.destroyAllWindows()
