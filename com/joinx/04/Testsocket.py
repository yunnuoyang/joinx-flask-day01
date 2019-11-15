import socket
# server=socket.gethostbyaddr("127.0.0.1")
# print(server)
# instance=socket.gethostname();
# print(instance)
s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    obj='欢迎访问菜鸟教程！'
    c.send(obj.encode()) #转化为bytes数据压缩传送
    c.close()  # 关闭连接