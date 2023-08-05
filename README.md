# Dataset-Tools
// Dataset type conversion   xml divide and txt filename VOC-to-COCO
## Labelme-VOC

### Usage

- First, the annotation file is converted to xml
- Then, the set of txt format file paths under voc is generated

### Convert to VOC-format Dataset

```bash
# It generates:
#   - data_dataset_voc/JPEGImages
#   - data_dataset_voc/Annotations
#   - data_dataset_voc/AnnotationsVisualization
./labelme2voc.py data_annotated data_dataset_voc --labels labels.txt
```

## Convert to COCO

### Usage

Modify the file path and save file path
