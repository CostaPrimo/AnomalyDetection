from flask import Flask, render_template, redirect, url_for, request
from forms import request_data

app = Flask(__name__)
__main__ = "__main__"
app.config['SECRET_KEY'] = 'eShVmYq3s5v8y/B?'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = request_data()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = request.form.get('data')
            return redirect(url_for('test2', data=data))
        return render_template('Home.html', title='Home', form=form)
    elif request.method == 'GET':
        return render_template('Home.html', title='Home', form=form)


@app.route('/Test')
def test():
    return "test"


@app.route('/Test2', methods=['POST','GET'])
def test2():
    data = request.args.get('data', None)

    return render_template('Test2.html', data=data, title="Test2")


def test():
    print("test")


def run_app(main):
    if __main__ == main:
        app.run(debug=True)
