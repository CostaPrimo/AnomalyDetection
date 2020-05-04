from flask import Flask, render_template, redirect, url_for, request
from forms import request_data
from . import LinkFacade
from Acquaintance import iLink, iLogic



app = Flask(__name__)
__main__ = "__main__"
app.config['SECRET_KEY'] = 'eShVmYq3s5v8y/B?'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = request_data()
    '''link = LinkFacade.linkFacade()'''
    print()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = request.form.get('data')
            print("Hejm")
            test1 = test900()
            print("hej")
            return redirect(url_for('test2', data=data, test=test1))
        return render_template('Home.html', title='Home', form=form)
    elif request.method == 'GET':
        return render_template('Home.html', title='Home', form=form)


@app.route('/Test')
def test():
    return "test"


@app.route('/Test2', methods=['POST','GET'])
def test2():
    data = request.args.get('data',  None)
    test4 = request.args.get('test', None)
    print(test)
    return render_template('Test2.html', data=data, title="Test2", test=test4)


def test900():
    print("test")
    Result = LinkFacade.linkFacade()
    hej = Result.printTest("tEST")
    return hej


def run_app(main):
    if __main__ == main:
        app.run(debug=True)



'''class RequestHandler:

    app = Flask(__name__)
    __main__ = "__main__"
    app.config['SECRET_KEY'] = 'eShVmYq3s5v8y/B?'

    def __init__(self, main):
        self.logic = iLogic.iLogic
        self.run_app(main)

    def inject_logic(self, iLogic):
        self.logic = iLogic

    @app.route('/', methods=['GET', 'POST'])
    def home(self):
        form = request_data()
        link = Link.LinkFacade.linkFacade().logic.getStreamStatus()
        print("test")
        if request.method == 'POST':
            if form.validate_on_submit():
                data = request.form.get('data')
                test = self.logic.getStreamStatus(data)
                return redirect(url_for('test2', data=data, test=test))
            return render_template('Home.html', title='Home', form=form)
        elif request.method == 'GET':
            return render_template('Home.html', title='Home', form=form)


    @app.route('/Test')
    def test(self):
        print("test")
        return "test"


    @app.route('/Test2', methods=['POST','GET'])
    def test2(self):
        print("test")
        data = request.args.get('data',  None)
        test = request.args.get('test', None)
        print(test)
        return render_template('Test2.html', data=data, title="Test2", test=test)


    def run_app(self, main):
        if self.__main__ == main:
            self.app.run(debug=True)
            '''
