from generativepy.bitmap import make_bitmap, Scaler
from generativepy.color import Color
from PIL import ImageDraw
import math
import random

SIN60 = math.sin(math.pi/3)

SIZE = 600
RANGE = 25
ITERATIONS = 1000000
VERTICES =  [(-7,1),
            (-4,1),
            (-4,3),
            (3,-2),
            (6,-2),
            (4,-4)]

def paint(image, pixel_width, pixel_height, frame_no, frame_count):
    scaler = Scaler(pixel_width, pixel_height,
                    width=RANGE*2, height=RANGE*2,
                    startx=-RANGE, starty=-RANGE)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, pixel_width, pixel_height),
                   fill=Color(0.2).as_rgbstr())
    x, y = 0, 0
    color = Color('green').as_rgbstr()
    for i in range(ITERATIONS):
        vertex = random.choice(VERTICES)
        x = (x + vertex[0])*3/4
        y = (y + vertex[1])*3/4
        u, v = scaler.user_to_device(x, y)
        draw.point((u, v), color)


make_bitmap("project5.png", paint, SIZE, SIZE)