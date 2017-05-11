from PIL import Image

img = Image.open('icon.jpg')
imgout = Image.new("RGBA", img.size)

imgout.paste(img, (0, 0))
pout = imgout.load()

for x in range(imgout.size[0]):
    for y in range(imgout.size[1]):
        r,g,b,a = pout[x, y]
        if r>200 and g>200 and b>200:
            pout[x, y] = (r,g,b,0)

imgout.save(r'icon.png', 'PNG')