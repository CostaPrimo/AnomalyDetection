from flask import Flask, render_template, redirect, url_for, request
from Logic import LogicFacade
from Persistence import PersistenceFacade


app = Flask(__name__)
__main__ = "__main__"
app.config['SECRET_KEY'] = 'eShVmYq3s5v8y/B?'
persistence = PersistenceFacade.persistenceFacade()
logic = LogicFacade.logicFacade()
logic.inject_persistence(persistence)

#Routing method, takes both GET and POST forms
#If its a POST method, it checks for streamtype, and if not null, runs the method getStreamStatus, and returns the result of that to the frontend.
@app.route('/', methods=['GET', 'POST'])
def home():
    data = ""
    confirmation = ""
    if request.method == 'POST':
        dropdown = request.form.get('dropdown', None)
        print("The value in dropdown: ", dropdown)
        if dropdown == None:
            print("None1")
            confirmation = 'Choose a type'
            return render_template('Home.html', title='Home', confirmation=confirmation)
        elif dropdown != 'null':
            print("kører getStreamStatus")
            data = getStreamStatus(dropdown)
            confirmation = "ready"
            print("Efter getStreamStatus")
            return render_template('Home.html', title='Home', data=data, confirmation=confirmation)
        elif dropdown == 'null':
            confirmation = 'Choose a type'
            return render_template('Home.html', title='Home', confirmation=confirmation)
    elif request.method == 'GET':
        return render_template('Home.html', title='Home')

#Returns the result of logic facades getStreamStatus
def getStreamStatus(streamtype):
    result = logic.getStreamStatus(streamtype)
    return result


if __main__ == __name__:
    app.run(debug=False)