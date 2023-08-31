# Assignment 2: Modify the YOLO model trained on the COCO dataset to detect people.

## Installing and Importing Dependencies
* Installing libraries such as Pytorch, matplotlib, etc.

## Loading Data from Roboflow
* Roboflow is a platform that assists in managing, annotating, and preparing data for training computer vision models. When you load data from Roboflow, you are typically loading a dataset that has been organized and annotated to train machine learning models, often for tasks like image classification, object detection, or segmentation.

* The folder Roboflow_Data contains the `Train` and `Test` images and labels used to train the YOLO model and detect to whether the image contains a Person or not.

## YOLO Model Train:
* !python train.py --img 640 --epochs 100 --data /Users/kushalbanda/4-1/Artificial_Intelligence_in_Industry/Assignments/Assignment-2/yolov5/Detect-People-1/data.yaml --weights yolov5s.pt --cache

## YOLO Model Detect:
* !python detect.py --weights yolov5s.pt --img 320 --conf 0.25 --source /Users/kushalbanda/4-1/Artificial_Intelligence_in_Industry/Assignments/Assignment-2/Detect-People-1/test/images --classes 0
