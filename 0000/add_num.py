from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('Anonymice Powerline.ttf', size=40)
    width, height = img.size
    draw.text((width-40, 0), '99', font = myfont, fill = 'red')
    img.save('result.png','png')
    return 0
if __name__ == '__main__':
    image = Image.open('github.png')
    add_num(image)