# Tag Framework System

Supported Features:

* General instance and video classification, detection, tracking, and search
* Supervised and self-supervised support
* Distributed traing
* Face detection: retina face

This is an initial design for a tag system, including training and inference.

1. Dataset: Providing dataloader for both image and video
2. Backbone: Providing various pretrained model selection for both image and
video support
3. Tasks: Providing various task trainers and inferences, including detection,
classification and search
4. Loss: Providing loss function selection and parameter adjuster, supporting
both image and video
5. Optimizer: Providing optimizer function selection and parameter adjuster,
supporting both image and video
6. Metrics: Providing evaluation functions for different tasks and models
7. Distributions: Providing CPU and GPU support versions, also extending to
Persia in the future

## Install

    python setup.py build
    python setup.py install
Or

    pip install .
## Usage

    export PYTHONPATH=YOURPATH/tag-framework-system/:$PYTHONPATH

### Distributed traing

### Video classification
#### S3D Network
Pretrained model
<a href="https://docs.corp.kuaishou.com/f/fcAD4isBuFBpJo5qmZCQRE040">Download Link</a>

#### P3D Network
Pretrained model
1. P3D-199 trained on Kinetics dataset:
<a href="https://docs.corp.kuaishou.com/file/fcACo6bOPgCxHGy9S6OSGIU34">Download Link</a>

2. P3D-199 trianed on Kinetics Optical Flow (TVL1):
<a href="https://docs.corp.kuaishou.com/file/fcACID9hgz3ym7sMB_Khyo1MM">Download Link</a>

3. P3D-199 trained on Kinetics600, RGB, 224&299:
Change the value of GAP kernel from 5 to 7 if 224, to 9 if 299
<a href="https://docs.corp.kuaishou.com/file/fcAB1W87jkrjOYGt5wLFF1vlJ">Download Link</a>

#### ebiz_item_classify Network
1. Pretrained model: Network trained on the set of kuaishou commodity with visual and language infomation
<a href="https://docs.corp.kuaishou.com/file/fcADbWgkfVb2b9eBvWUdm5jkb">Download Link</a>

2. Use the following command to fine tune the model with the latest ebiz data:

    cd tag_framework/networks/ebiz_item_classify/
    
    sh at012_auto_train.sh
    
#### C3D Network
Currently, we do not have pretrained C3D network.

### Video representation learning

### Video Detection

### Video Tracking

### Video Search

### Face Detection
You can use retina face now, just look at example/retinaface/test_face.py 

Copyright (c) 2020, Kuaishou. All rights reserved.
