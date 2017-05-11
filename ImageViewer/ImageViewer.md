基于TkInter的图片浏览器
=====
## PIL && TkInter
PIL是Python默认的图像库，TkInter是Python默认的图形界面库，Python3开始成为内建库。Python2需要先安装PIL和TkInter包。另外对TKInter包，在Python2和Python3中包名大小写不同，Python2中是Tkinter，Python3中是tkinter，请按照Python版本修改正确的包名。  

## 使用方法
```txt
python3 path_to/image.py [path]
```
默认浏览当前目录下的图片，指定 **\[path\]** 参数后浏览该目录下的图片或直接显示该图片文件。  
鼠标单击图片切换下一张，方向键&larr;浏览上一张，方向键&rarr;浏览下一张。