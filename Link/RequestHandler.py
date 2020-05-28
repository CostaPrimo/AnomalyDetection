from flask import Flask, render_template, redirect, url_for, request
from forms import request_data
from Logic import LogicFacade
from Persistence import PersistenceFacade


app = Flask(__name__)
__main__ = "__main__"
app.config['SECRET_KEY'] = 'eShVmYq3s5v8y/B?'
persistence = PersistenceFacade.persistenceFacade()
logic = LogicFacade.logicFacade()
logic.inject_persistence(persistence)


@app.route('/', methods=['GET', 'POST'])
def home():
    #form = request_data()
    data = ""
    if request.method == 'POST':
        dropdown = request.form.get('dropdown', None)
        print("The value in dropdown: ", dropdown)
        if dropdown == None:
            print("None1")
            return render_template('Home.html', title='Home')
        elif dropdown != 'null':
            print("kører test900")
            data = test900(dropdown)
            print("Efter test900")
            return render_template('Home.html', title='Home', data=data)
        elif dropdown == 'null':
            return render_template('Home.html', title='Home')
    elif request.method == 'GET':
        return render_template('Home.html', title='Home')



@app.route('/Test')
def test():
    return "test"


@app.route('/Test2', methods=['POST', 'GET'])
def test2():
    data = request.args.get('data',  None)
    test4 = request.args.get('test', None)
    return render_template('Test2.html', data=data, title="Test2", test=test4)


def test900(streamtype):
    result = logic.getStreamStatus(streamtype)
    print(result)
    return result


if __main__ == __name__:
    app.run(debug=False)
