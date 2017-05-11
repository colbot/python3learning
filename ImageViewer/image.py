# -*- coding:utf-8 -*-
import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

icon_b64 = \
b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAACf1BMVEVHcEz5kDSoz1FJml7oi2Gr'\
b'0VZTmKbs2dG2M3zKxcGtoZX5lDyvSH80krk/mFez0Gm31HBrNYNYob3lOUb+/jV3PYJxPobsMkL8'\
b'/nr9+kBfoWz39F91SYiv0mBJmVw2lbq4N3/fTV39/UboQE46lrq6UoxUnnByQob8/lS2O39dpXHy'\
b'oVq81H/8/1XoSFn3mkb1qWVCmlPpOEjoZGHrPUVuNoNdMoDiR1FsRob9/HL9/U3QSlZCmLrjOUY7'\
b'lrhHml78/Vj2lkH6lT23U461PYGxR4VImLNCl7n8/nk6lbuw1GJ8UpBDm1s+lbqu0V5yP4W4OIFB'\
b'mVe1QIB/WJTkWGU5lFb4ejD+/jr4lkFsOIMpho/+/2ynz01zrmNqWpWNwErs8mDVTGMuap30+DX0'\
b'4mehLXbiMEKz1Dy4J175my4UaCKv1CD3lxswDk+0FzLqNBdqFU5VmSwpOHMdaFr9kC///y/+jy3+'\
b'kATtEwTsMD8gexAEVTgNFl7//y04l1D5dieyBhwHWEb+jyUqgAiLvwiTAhgPJGVLAjyrAhkxkrtQ'\
b'ASg7ix0hf5C3LnxpMIL/jy778yhiCkntMD/+/jJqLoLvMhACUi6mwgXNqQfBBwgHEkUMElXlEQXs'\
b'GgOMv0HtKzen0EwJXzj1+SmzIFztFwypBSUYGWJOBkT6nwem0AcmaZ2z1gscdBA1lEldLH5mKXqn'\
b'0TMykEvkKjtAAjgifxmqAhOhJ3AMZEUbJGvtLAuzCyfuLAxcKHglbaBKkxvnKjYRYx6fzBG2Bx75'\
b'owep0Qb6hwzvigMEPi4GVREkBkO3jAOp0gf3bwMDOS32YQLwjAIFRTj5bgPODBELGVEXBDjg84Dt'\
b'AAAAdHRSTlMA4eFnHNoeAeAFDNsd4dkbOtdLZf1SZfob6SpXJ7FS+PkszsndR4R1a706PSpzU6Y0'\
b'6N5m8+zyQh0+yhHCuceVXbLmVck2NqY46qE4zb64lerxpzw9+vv2t8n8R+FWhPeOhvj7bPf4/Pv4'\
b'/fHw/ePr1efT07V8U7gAAAI5SURBVHheddBldxpBGIbhQZcFUhIkBGiaNmncGqFJ3d3d3d0Wd5e4'\
b'e93d3d39B3WGYQJpDvdHnos5L4ABFU6ZKiodBRJWKGL0ekaUUAhXN6CYUnrQNK5KVsIFXBba9XoR'\
b'F6Rp8jRpsX3EBKVJmbUcASRY3HWZ8hb52DFk52aZmmHlFRgwrO0qnc1m02WSN0qUEWCqXIlf2KPS'\
b'RZJPxjslgzvqRJuDgSe4LzbqcMUAJzOZMDj7yNHAuA0EtOSRG8ubo8D4xOE2EGBTzY4CqqKSAGPb'\
b'OwJsq4opvNNi8Zadt2EvIOj7ajC8aTwN27a5SEKjr89YKhAIdj92Op2vu3qNxu+G951XULvYbN7c'\
b'IgCyBXWoM+eCweC9rt6+Xz8+d1yC3TyJ4iWDfLjGxO9D+zs7vrxFOy4dDK/rFz6f72CVZp/X630F'\
b'dxwvBu43hcPhw9XqIx6P5/nxGJjevwcCgTsHjh7be9VsNtcQkQ6mLY7b//b8+dn+EQtyJJ2dD3/m'\
b'jqYLsE891u5vlvaXd2E1m9jr2QuT0X8lFIsV2huwp+et1u4PFsupW9dgZRskEiHALUtprYddh8Dv'\
b'QsCOGlIAolWvgSsG/me1LgLs8/l4pxT1BPgvh0K1LgLswwAulYCHcIfiAQGcgaB19NZQpLUr/gND'\
b'UyK7dmMSBkk5S/CVahBNgYQ2lU8An1OGdnQCeSN3Ue48ioCRfKogZxJHTYH4KEAJF2Awi8YfDIqS'\
b'zok8MBMkipZOzMgYLwXx/QNXjVOosgZZhAAAAABJRU5ErkJggg=='

event_name = {
    '2': "KeyPress",
    '3': "KeyRelease",
    '4': "ButtonPress",
    '5': "ButtonRelease",
    '6': "Motion",
    '7': "Enter",
    '8': "Leave",
    '9': "FocusIn",
    '10': "FocusOut",
    '12': "Expose",
    '15': "Visibility",
    '17': "Destroy",
    '18': "Unmap",
    '19': "Map",
    '21': "Reparent",
    '22': "Configure",
    '24': "Gravity",
    '26': "Circulate",
    '28': "Property",
    '32': "Colormap",
    '36': "Activate",
    '37': "Deactivate",
    '38': "MouseWheel"
}


def show_image(view, image_list, cur):
    global _img
    global app
    global screen_w, screen_h
    if not image_list:
        label['text'] = 'No Image'
        label['padx'] = 10
    else:
        if _img:
            del _img
        if cur >= len(image_list):
            cur -= len(image_list)
        limg = Image.open(image_list[cur])
        w, h = limg.size
        resize = False
        if w > screen_w:
            h = (screen_w * h) // (w * 2)
            w = screen_w // 2
            resize = True
        if h > screen_h:
            w = (screen_h * w) // (h * 2)
            h = screen_h // 2
            resize = True
        if resize:
            limg = limg.resize((w, h), Image.ANTIALIAS)
        _img = ImageTk.PhotoImage(limg)
        view.config(image=_img)
        view.config(text=None)
        view.config(padx=0)
        a, b = os.path.split(image_list[cur])
        app.title(b)
        app.geometry("%sx%s+%s+%s" % (w, h, (screen_w-w)//2, (screen_h-h)//2))
    return cur


def switch_image(e):
    global index
    global label
    global images
    global event_name
    forward = 0
    ename = event_name[e.type]
    if ename == "KeyPress":
        if e.char == 'q' or e.char == 'Q':
            app.destroy()
        elif e.keysym == "Left":
            forward = -1
        elif e.keysym == "Right":
            forward = 1
    elif ename == "ButtonPress":
        if e.num == 1:
            forward = 1
        elif e.num == 3:
            forward = -1
    if forward:
        index += forward
        index = show_image(label, images, index)


# main entry
image_ext = ['.jpg', '.png', '.gif', '.tif', '.bmp']

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

if os.path.isfile(path):
    files = [path]
else:
    files = [path+os.sep+f for f in os.listdir(path)]
images = [f for f in files if any(f.endswith(ext) for ext in image_ext)]
del files

app = tk.Tk()
app.withdraw()
app.title('Photo')
app.geometry("300x200+200+200")
screen_w = app.winfo_screenwidth()
screen_h = app.winfo_screenheight()
img = tk.PhotoImage(data=icon_b64)
ret = app.tk.call('wm', 'iconphoto', app._w, img)

index = 0
_img = None
label = tk.Label(app)

index = show_image(label, images, index)
label.pack(expand="yes", fill="both")
label.bind("<Button>", switch_image)
app.bind("<Key>", switch_image)

app.deiconify()
app.mainloop()
