# NAMING CONVENTION

This is a convention of **naming for training modules or log directories**.
Each digits of filename means various environments.

- Each name should be in the following format:

     [basename]_<[network_model](#1-network-model)> <[pretrained_model](#2-pre-trained-weight)> <[classes](#3-classes)> <[freeze](#4-freeze)> <[loss-func](#5-loss-function)> <[learning-rate](#6-learning-rate)> <[data-manipulation](#7-data-manipulation)>


## Various Environments

### 1. Network Model
 - 0 : YOLOv3

### 2. Pre-trained Weight
 - 0 : [YOLOv3-416 pre-trained by COCO](https://pjreddie.com/darknet/yolo/)

### 3. Classes
 - 0 : Only direct child objects of frame(exclude child objects of rider)
    
    **# of classes : 12**
    ```
    rider
    person-group-far-away
    rider+vehicle-group-far-away
    bicycle-group
    pedestrian
    tricycle-group
    buggy-group
    scooter-group
    motorbike-group
    motorbike
    bicycle
    wheelchair-group
    ```
 - 1 : All objects(include child objects of rider)
 
    **TODO: update class info**

### 4. Freeze
 - 0 : Unfreeze all layers

### 5. Loss function
 - 0 : mse

### 6. Learning rate
 - 0 : ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=10, verbose=1)

### 7. Data manipulation
 - 0 : Default dataset

## Fixed Environments
   ```
       Train data = /data/train
       Val data, test data = split /data/val ratio=0.5 random.seed(0)

       # of Train images : 32879
       # of Val images : 2160
       # of Test images : 2106
   ```