from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/memory')
def memory():
    return render_template("memory.html" , image_num=5)


@app.route('/widow')
def widow():
    return render_template('black-widow.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
