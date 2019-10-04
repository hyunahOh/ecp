import json
import os
import glob

ecp_to_yolo_classes = {
    'rider':'1',
    'person-group-far-away':'0',
    'rider+vehicle-group-far-away':'1',
    'pedestrian': '0'
}

def ecp_to_yolo(source, frame):
    destf.writelines('{}.png'.format(os.path.splitext(source)[0]))

    for c in frame['children']:
        if c['identity'] in ecp_to_yolo_classes:
            destf.writelines(' {},{},{},{},{}'.format(
                c['x0'],
                c['y0'],
                c['x1'] ,
                c['y1'],
                ecp_to_yolo_classes[c['identity']]))
    destf.writelines('\n')

destf = open('/home/ecp/keras-yolo3/train_op2.txt', 'w')

for filename in glob.iglob('/home/ecp/keras-yolo3/data/train/*/*.json', recursive=True):
    print(filename)
    frame = json.load(open(filename, 'r'))
    ecp_to_yolo(filename, frame)
