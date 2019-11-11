 #   coding:utf-8
from flask import Flask

# 创建flask的应用对象
#  __name__表示当前模块名字 即当前文件名
#  flask模块名：flask以这个模块所在的目录为总目录，
# 默认这个目录的static为静态目录，template为模板目录
app=Flask(__name__)
@app.route("/")
def index():
    "定义的视图函数"
    return "hello flask";
if __name__ == '__main__':
    # 启动flask函数
    app.run()