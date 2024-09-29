# YOLOv8 Image Recognition

#### Introduction
Welcome to the YOLOv8 repository! Based on the YOLOv8 algorithm, this warehouse realizes efficient real-time object detection. YOLOv8 is the latest version in the You Only Look Once series, which improves the performance and speed of object detection by improving the network architecture and training strategy.

#### Features
1. **Real-time Object Detection:** YOLOv8 enables real-time object detection, accurately identifying multiple objects in an image.
2. **Multi-category support:**  Common object categories are supported, which can be easily extended to custom categories.
3. **Ease of use:** With simple configuration and command line arguments, users can easily use and customize YOLOv8 models.
4. **Performance Optimization:** Based on the latest deep learning frameworks and optimization techniques, the model is guaranteed to achieve excellent performance on a variety of hardware.

### Requirements

1. Python 3.8+
2. PyTorch 1.8+
3. CUDA Toolkit (if using GPU)

#### Instructions for Use

1. Install Dependencies: Install the required dependencies by running the following command from the project root:
`pip install -r requirement.txt`
2. Download the pre-trained model: [Official model library](https://docs.ultralytics.com/models/yolov8/#supported-tasks-and-modes) download for YOLOv8 training model, And save it to the models/ directory.
2. Run Prediction:
`python predict.py --image_path /path/to/image.jpg` Change the --image_path argument to the path of the image to be recognized.
3. Custom configuration: Modify the _config.yaml_ file according to the project requirements to adjust the model configuration, category information, etc.

#### Example

Some example images along with the corresponding prediction results are provided in the examples/ directory for the user's reference.
For more in [Examples](https://docs.ultralytics.com/modes/predict/)
