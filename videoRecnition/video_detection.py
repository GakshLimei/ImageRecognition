import cv2
from ultralytics import YOLO

# 加载YOLOv8模型
model = YOLO('../yolo v8 models/yolov8n.pt')

# 打开视频文件
video_path = "D:\\Administrator\\Videos\\Captures\\(27) #AFCCup - Full Match - Group F _ Phnom Penh Crown FC (CAM) vs Dynamic Herb Cebu FC (PHI) - YouTube.mp4"
cap = cv2.VideoCapture(video_path)

# 设置视频分辨率
desired_width = 1280
desired_height = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

# 遍历视频帧
while cap.isOpened():
    # 从视频中读取一帧
    success, frame = cap.read()

    if success:
        # 在该帧上运行YOLOv8推理
        results = model(frame)

        # 在帧上可视化结果
        annotated_frame = results[0].plot()

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
