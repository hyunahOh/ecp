import json
import os
import glob

ecp_to_yolo_classes = {'pedestrian': '0', 'rider': '1', 'person-group-far-away' : '0', 'rider+vehicle-group-far-away':'1',}


# def ecp_to_yolo(source, frame):
#     for c in frame['children']:
#         if c['identity'] in ecp_to_yolo_classes:
#             destf.writelines('{} {:08.6f} {:08.6f} {:08.6f} {:08.6f}\n'.format(
#                 ecp_to_yolo_classes[c['identity']],
#                 (c['x0']+c['x1'])/3840,
#                 (c['y0']+c['y1'])/2048,
#                 (c['x1']-c['x0'])/1920 ,
#                 (c['y1']-c['y0'])/1024))
#     destf.writelines('\n')


#path = '/home/haoh/ECPB-darknet/input_data_yolo/train/'

destf = open('/home/ecp/darknet/val.txt', 'w')

for filename in glob.iglob('/home/ecp/keras-yolo3/data/val/*/*.json', recursive=True):
    frame = json.load(open(filename, 'r'))
    basename = os.path.basename(filename)
    path = os.path.dirname(os.path.abspath(filename))
    name = os.path.splitext(basename)[0]

    # destf = open(path+'/'+name+'.txt', 'w')
    destf.writelines(path+'/'+name+'.png\n')
    # print(path+'/'+name+'.png')
    # ecp_to_yolo(filename, frame)
