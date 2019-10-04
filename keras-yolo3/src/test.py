from PIL import Image, ImageDraw, ImageFont
# get an image
im = Image.open('/home/ecp/keras-yolo3/data/train/bologna/bologna_00832.png').convert('RGBA')

draw = ImageDraw.Draw(im)
draw.rectangle(((340,463), (406,678)), outline="#ff8888", width=5)
draw.rectangle(((262,423), (369,741)), outline="#ff8888", width=5)
draw.rectangle(((1313,501), (1341,612)), outline="#ff8888", width=5)
draw.rectangle(((1284,515), (1318,619)), outline="#ff8888", width=5)
draw.rectangle(((1266,510), (1300,618)), outline="#ff8888", width=5)
draw.rectangle(((1266,510), (1300,618)), outline="#ff8888", width=5)
draw.rectangle(((906,534), (928,592)), outline="#ff8888", width=5)
del draw

im.save('/home/ecp/keras-yolo3/output-occluded-40.png')