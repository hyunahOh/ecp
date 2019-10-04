import os
import glob
from PIL import Image
from yolo import YOLO

class_name = [
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

def write_result(yolo, image):
    out_boxes, out_scores, out_classes = yolo.detect_image(image)

    for i, c in reversed(list(enumerate(out_classes))):
        predicted_class = out_classes[i]
        box = out_boxes[i]
        score = out_scores[i]
        destf.writelines('{} {} {} {} {} {}\n'.format(
            class_name[predicted_class],
            score,
            box[1],
            box[0],
            box[3],
            box[2]))

if __name__ == '__main__':
    yolo = YOLO()
    for filename in glob.iglob('/home/ecp/mAP/input/images-optional/*.png', recursive=True):
        basename = os.path.basename(filename)
        name = os.path.splitext(basename)[0]

        path = '/home/ecp/mAP/input/detection-results/'
        destf = open(path + name + '.txt', 'w')

        try:
            image = Image.open(filename)
        except:
            print('Open Error! Try again!')
            continue
        else:
            write_result(yolo, image)