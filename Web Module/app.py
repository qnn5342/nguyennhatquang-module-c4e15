from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'hello world 2'

@app.route('/sayhi/<name>')
def haha(name):
    return name + " dai ca"

@app.route('/sum/<int:input1>/<int:input2>')
def sum(input1, input2):
    return str(input1+ input2)

@app.route('/html')
def heading():
    return "<h1>Sexy ladies</h1>"

@app.route('/blog')
def blog():
    article_name= "Thơ con cóc"
    posts = [{'Content': "Phấn khởi",
    "author": "Nguyên"
    },
    {'Content': "Chỉ là gió thoảng đầu môi",
    "author": "TUấn ANh"
    },
    {'Content': "Phấn khởi",
    "author": "Nguyên"
    },
    {'Content': "Phấn khởi",
    "author": "Nguyên"
    },
        ]

    return render_template('blog.html', articletitles = article_name,posts = posts)


if __name__ == '__main__':
  app.run(debug=True)
