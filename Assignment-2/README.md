# Assignment 2: Modify the YOLO model trained on the COCO dataset to detect people.

## Installing and Importing Dependencies
* Installing libraries such as Pytorch, matplotlib, etc.

## Loading Data from Roboflow
Roboflow is a platform that assists in managing, annotating, and preparing data for training computer vision models. When you load data from Roboflow, you are typically loading a dataset that has been organized and annotated to train machine learning models, often for tasks like image classification, object detection, or segmentation.
Here's a brief explanation of the data loaded from Roboflow:

### Images:
* These are the visual data points that your model will learn from. Images are usually in formats like JPEG or PNG. They represent the input data for your model to make predictions on.
### Annotations:
* Annotations are metadata associated with images that provide additional information, often in the form of bounding boxes, polygons, or labels. Annotations are crucial for tasks like object detection, where you need to specify where objects are located in the images.
### Labels:
* Labels are the class names or categories that your model is expected to predict. For example, if you're training an image classification model. 
* Labels in our case is "Person". 
### Bounding Boxes:
* For object detection tasks, bounding boxes define rectangular regions around objects of interest within an image. They specify the location (coordinates) and size of the objects.

## YOLO Model Train:
* !python train.py --img 640 --epochs 100 --data /Users/kushalbanda/4-1/Artificial_Intelligence_in_Industry/Assignments/Assignment-2/yolov5/Detect-People-1/data.yaml --weights yolov5s.pt --cache

## YOLO Model Detect:
* !python detect.py --weights yolov5s.pt --img 320 --conf 0.25 --source /Users/kushalbanda/4-1/Artificial_Intelligence_in_Industry/Assignments/Assignment-2/Detect-People-1/test/images
