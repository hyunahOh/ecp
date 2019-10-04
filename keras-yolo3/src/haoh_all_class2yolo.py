import json
import os
import glob


ecp_to_yolo_classes = {}
child_dict = {}
count = 1
count2 = 1
destf = open('/home/ecp/keras-yolo3/class_name.txt', 'w')
tags = {}
bad = 0
good = 0
rainy_pedes = 0
pedes_sub_class = {}


def get_data_num(source, frame):

    for c in frame['children']:
        if not c['tags']:
            c_tag = ''
        else:
            c_tag = ', '.join(c['tags'])

        if not frame['tags']:
            f_tags = ''
        else:
            f_tags = '(f) '.join(frame['tags'])

        global rainy_pedes
        if c['identity'] == 'pedestrian':
            for p in c['tags']:
                if not p in pedes_sub_class:
                    pedes_sub_class[p] = 1
                else:
                    pedes_sub_class[p] += 1

        if not c['identity']+c_tag in ecp_to_yolo_classes:
            ecp_to_yolo_classes[c['identity']+c_tag] = 1
            destf.writelines('{}\n'.format(c['identity']+c_tag))
        else:
            ecp_to_yolo_classes[c['identity']+c_tag] = ecp_to_yolo_classes[c['identity']+c_tag] + 1

        for gc in c['children']:
            global count2
            str = gc['identity'] + ":" +c['identity']
            if not str in child_dict:
                child_dict[str] = count2
                destf.writelines("i'm {} child of {}\n".format(gc['identity'], c['identity']))
            else:
                child_dict[str] = child_dict[str] + 1

def get_tags(frame):
    global good
    if not frame['tags']:
        good+=1
    else:
        for t in frame['tags']:
            global bad

            if not t in tags:
                tags[t] = 1
                bad+=1
            else:
                tags[t] = tags[t]+1
                bad+=1

for filename in glob.iglob('/home/ecp/keras-yolo3/data/train/*/*.json', recursive=True):
    frame = json.load(open(filename, 'r'))
    basename = os.path.basename(filename)
    name = os.path.splitext(basename)[0]
    # get_tags(frame)
    get_data_num(filename, frame)

# print(ecp_to_yolo_classes)
# print(child_dict)
# print(tags)
# # print(good)
# # print(bad)
# # print(rainy_pedes)

print(pedes_sub_class)