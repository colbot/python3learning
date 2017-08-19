支持文件上传的HTTPServer
=====

## 默认
Python 默认的 **SimpleHTTPServer** 用起来很方便，偶尔需要传送文件时直接从 Python 启动一个 HTTPServer 即可，无需其他工具。启动命令为
```python
python -m SimpleHTTPServer [port]
```
一般 *[port]* 选择 *1024* 以后的端口，防止权限不足，默认为 *8000*。  

Python3 默认为 **http.server** ，启动命令为
```python
python3 -m http.server [port]
```

## 改进
Python自带的 HTTP 服务器只有页面显示和文件下载功能，不支持文件上传，使用起来多有不便，这里在默认 SimpleHTTPServer 的基础上增加文件上传功能。  
实现方式为重载 `SimpleHTTPRequestHandler` 的 `do_POST` 和 `list_directory` 方法。其中在 `do_POST` 方法中实现文件保存，在 `list_directory` 方法中增加一个 POST 文件的表单。具体实现方式见 [httpServer.py](httpServer.py)  
很多时候通过多层跳板登录时，无法直接通过 scp 拷贝文件，可以先通过终端将通过复制粘贴将该文件保存。然后执行该脚本启动一个可以上传下载的页面服务。
```python
python3 httpServer.py [port]
```