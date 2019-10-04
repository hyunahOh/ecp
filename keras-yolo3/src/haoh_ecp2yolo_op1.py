import json
import os
import glob

ecp_to_yolo_classes = {
    'rider':'0',
    'person-group-far-away':'1',
    'rider+vehicle-group-far-away':'2',
    'bicycle-group':'3',
    'pedestrian': '4',
    'tricycle-group': '5',
    'buggy-group': '6',
    'scooter-group': '7',
    'motorbike-group': '8',
    'motorbike': '9',
    'bicycle': '10',
    'wheelchair-group': '11'
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

destf = open('/home/ecp/keras-yolo3/val_op1.txt', 'w')

for filename in glob.iglob('/home/ecp/keras-yolo3/data/val/*/*.json', recursive=True):
    print(filename)
    frame = json.load(open(filename, 'r'))
    ecp_to_yolo(filename, frame)
