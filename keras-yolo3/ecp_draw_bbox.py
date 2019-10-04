# module for drawing ground truth bounding boxes (to be used in ecp task)

import colorsys
import os
from timeit import default_timer as timer

import numpy as np
from PIL import Image, ImageFont, ImageDraw
import os
from src.yolo3.utils import letterbox_image

class BboxDrawing(object):
    _defaults = {
        "gt_path": 'train_op1.txt',
        "classes_path": 'model_data/ecp_classes_op1.txt',
        "model_image_size" : (416, 416),
    }
    
    def __init__(self):
        self.__dict__.update(self._defaults)
        self.class_names = self._get_class()
        self.images, self.boxes, self.classes = self.generate()

    def _get_class(self):
        classes_path = os.path.expanduser(self.classes_path)
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

    def generate(self):
        images = []
        boxes = []
        classes = []
        gt_path = os.path.expanduser(self.gt_path)
        f = open(gt_path)
        for n in range(5):   # just for 10 pictures for now
            line = f.readline()
            #if not line: break
            info = line.split(' ')
            if len(info) == 1: continue    # skip images without bounding boxes
            images.append(info[0])          # image file name
            boxes_in_img = []
            classes_in_img = []
            for i in range(len(info[1:])):     # only bounding boxes in that image
                box = [int(x) for x in info[i+1].split(',')]    # length 5
                boxes_in_img.append(box[:-1])
                classes_in_img.append(box[-1])
            boxes.append(boxes_in_img)
            classes.append(classes_in_img)
        
        f.close()
        
        # Generate colors for drawing bounding boxes.
        hsv_tuples = [(x / len(self.class_names), 1., 1.)
                      for x in range(len(self.class_names))]
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
        self.colors = list(
            map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
                self.colors))
        np.random.seed(10101)  # Fixed seed for consistent colors across runs.
        np.random.shuffle(self.colors)  # Shuffle colors to decorrelate adjacent classes.
        np.random.seed(None)  # Reset seed to default.

        return images, boxes, classes
        
    def draw_bbox(self):
        for i in range(len(self.images)):
            image = Image.open(self.images[i])
            #boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
            image_data = np.array(image, dtype='float32')
            print(image_data.shape)
            image_data /= 255.
            image_data = np.expand_dims(image_data, 0)

            print('Found {} boxes for {}'.format(len(self.boxes[i]), 'img'))

             
            font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
                                      size=np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))
            thickness = (image.size[0] + image.size[1]) // 300

            for bi, box in reversed(list(enumerate(self.boxes[i]))):
               cls = self.classes[i][bi]

               label = str(cls) 
               draw = ImageDraw.Draw(image)
               label_size = draw.textsize(label, font)

               left, bottom, right, top = box
               #top, left, bottom, right = box
               #top = max(0, np.floor(top + 0.5).astype('int32'))
               #left = max(0, np.floor(left + 0.5).astype('int32'))
               #bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
               #right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
               print(label, (left, top), (right, bottom))

               if top - label_size[1] >= 0:
                   text_origin = np.array([left, top - label_size[1]])
               else:
                   text_origin = np.array([left, top + 1])

               # My kingdom for a good redistributable image drawing library.
               for t in range(thickness):
                   draw.rectangle(
                       [left + t, top + t, right - t, bottom - t],
                       outline=self.colors[t])
               draw.rectangle(
                   [tuple(text_origin), tuple(text_origin + label_size)],
                   fill=self.colors[t])
               draw.text(text_origin, label, fill=(0, 0, 0), font=font)
               del draw
                
               file_name = 'result{}.jpg'.format(i)
               image.save(file_name)





if __name__ == '__main__':
    Bbox = BboxDrawing()
    Bbox.draw_bbox()
    print(Bbox.boxes)
