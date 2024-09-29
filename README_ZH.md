# YOLOv8 图像识别

#### 介绍
欢迎来到 YOLOv8 图像识别项目仓库！本仓库基于 YOLOv8 算法，实现了高效的实时目标检测。YOLOv8 是 You Only Look Once（你只需看一次）系列中的最新版本，通过改进网络结构和训练策略，提高了目标检测的性能和速度。

#### 功能特性
1. **实时目标检测：** YOLOv8 实现了实时目标检测，能够在图像中准确地识别多个物体。
2. **多类别支持：** 支持常见的物体类别，可轻松扩展到自定义类别。
3. **易用性**： 通过简单的配置和命令行参数，用户可以方便地使用和定制 YOLOv8 模型。
4. **性能优化**： 基于最新的深度学习框架和优化技术，确保模型在各种硬件上都能获得卓越性能。

### 需要

1. Python 3.8+
2. PyTorch 1.8+
3. CUDA Toolkit (如果使用 GPU)

#### 使用说明

1.  安装依赖： 在项目根目录下运行以下命令安装所需依赖：
`pip install -r requirement.txt`
2. 下载预训练模型： 在 [官方模型库](https://docs.ultralytics.com/models/yolov8/#supported-tasks-and-modes) 下载适用于 YOLOv8 的预训练模型，并将其保存到 models/ 目录下。
2.  运行预测： 使用以下命令运行图像识别：
`python predict.py --image_path /path/to/image.jpg`修改 --image_path 参数为待识别图像的路径。
3.  自定义配置： 根据项目需求修改 _config.yaml_ 文件，调整模型配置、类别信息等。

#### 示例

在 examples/ 目录下提供了一些[示例](https://docs.ultralytics.com/zh/modes/predict/)图像以及相应的预测结果，供用户参考。

