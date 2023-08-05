"""
Version: 1.0
Date: 20230802

Description:
used to split the dataset into cases than training
Training proportions for the partition under Mian are generated
Mian folder needs to be created in advance, with xml format and images


Need file tree
# VOC 2007
# ├── Annotations  # *.xml File
# │   ├── image1.xml
# │   ├── image2.xml
# │   └── ...
# ├── JPEGImages  # *.jpg File
# │   ├── image1.jpg
# │   ├── image2.jpg
# │   └── ...
# └── ImageSets
#     └── Main    # *.txt File
#         ├── train.txt
#         ├── val.txt
#         └── ...

20230804

In addition, if you plan to train with yolov5 and above models, you can use the data_v5 file to generate the required format for the model
"""



# Divide the VOC dataset
import os
import random

datasets_path = r'VOC2007/'  

trainval_percent = 0.8
train_percent = 0.9
xml_path = datasets_path + 'Annotations'
txtsavepath = datasets_path + 'ImageSets/Main'
total_xml = os.listdir(xml_path)

num = len(total_xml)
list1 = range(num)
tmtp = int(num * trainval_percent)
trp = int(tmtp * train_percent)
trainval = random.sample(list1, tmtp)
train = random.sample(trainval, trp)

with open(datasets_path + 'ImageSets/Main/trainval.txt', 'w') as ftrainval, \
        open(datasets_path + 'ImageSets/Main/test.txt', 'w') as ftest, \
        open(datasets_path + 'ImageSets/Main/train.txt', 'w') as ftrain, \
        open(datasets_path + 'ImageSets/Main/val.txt', 'w') as fval:

    for i in list1:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)
