import json
import os
import glob

ecp_classes = [
    "rider",
    "person-group-far-away",
    "rider+vehicle-group-far-away",
    "bicycle-group",
    "pedestrian",
    "tricycle-group",
    "buggy-group",
    "scooter-group",
    "motorbike-group",
    "motorbike",
    "bicycle",
    "wheelchair-group"
]

def ecp_to_yolo(source, frame):
    for c in frame['children']:
        if c['identity'] in ecp_classes:
            destf.writelines('{} {} {} {} {}\n'.format(
                c['identity'],
                c['x0'],
                c['y0'],
                c['x1'] ,
                c['y1']))

for filename in glob.iglob('/home/ecp/keras-yolo3/data/val/amsterdam/*.json', recursive=True):
    basename = os.path.basename(filename)
    path = '/home/ecp/mAP/input/ground-truth/'
    name = os.path.splitext(basename)[0]
    destf = open(path + name + '.txt', 'w')
    frame = json.load(open(filename, 'r'))
    ecp_to_yolo(filename, frame)
