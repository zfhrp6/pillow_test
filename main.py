# coding: utf-8

def random_image():
    from PIL import Image, ImageFilter, ImageDraw, ImageFont
    from random import randint

    img = Image.new('1', (800, 480), 1)

    draw = ImageDraw.Draw(img)
    draw.line((0, img.height, img.width, 0), fill=1, width=3)

    color = 0
    for i in range(1000):
        x0,y0,x1,y1 = randint(0, img.width), randint(0, img.height), randint(0, img.width), randint(0, img.height)
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        draw.rectangle((x0, y0, x1, y1), fill=color)
        color ^= 1

        x0,y0,x1,y1 = randint(0, img.width), randint(0, img.height), randint(0, img.width), randint(0, img.height)
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        draw.ellipse((x0, y0, x1, y1), fill=color)
        color ^= 1
    return img


def main():
    import sys
    img_name = sys.argv[1] if len(sys.argv) > 1 else 'imaga_output.bmp'

    img = random_image()
    img.save(img_name)


if __name__ == '__main__':
    main()

