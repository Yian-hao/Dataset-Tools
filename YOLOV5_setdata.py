# 用于将数据集划分成案例比训练，
"""
将标准的VOC转化为可以用YOLOv5 训练的格式，生成Main 里的三个txt文本，但是，前提要有相应的文件夹，然后接着用另外一个生成label 即文件路径

VOC2007
|—— Annotations # *.xml File
| |——000001.xml
| |——000002.xml
| |——……
|—— JPEGImages # *.jpg File
| |——000001.jpg
| |——000002.jpg
| |——……
|—— ImageSets # txt filename
| |——Main


"""



# 划分VOC数据集
import os
import random

datasets_path = r'VOC2007/'  # 数据集路径

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