from filecmp import cmp

from flask import Flask, redirect, abort

app = Flask(__name__,
            static_url_path="/python",  #访问静态资源的url地址，默认是static
            static_folder="static", # 静态文件的目录,默认就是static
            template_folder="templates", # 模板文件的目录，默认是templates
            )
@app.route('/')
def hello_world():
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']
    print(days)
    print('你好，世界')
    return '你好，世界!'
@app.route('/user')
def getUser():
    total='abc'+\
        'mnq'+\
        'happy'
    print(total)
    if True:
        print('糟糕透顶')
        print('相同代码块的代码缩进空格必须相同')
    else:
        print('世界很美好')
    return 'joinx-hello,to start python'
@app.route('/dynimic/<path>')
def dynimicPath(path):
   # return 'app' % path
    return redirect('http://www.baidu.com')
@app.route('/user/<id>')
def get_user(id):
        counter = 100  # 赋值整型变量
        miles = 1000.0  # 浮点型
        name = "John"  # 字符串
        print(counter);print(name);print(miles)


        abort(404) # 将404的状态码返回给web浏览器
        return '<h1>Hello, %s</h1>'

if __name__ == '__main__':
    app.run()
