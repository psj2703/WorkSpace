from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'This is Home'

@app.route('/hello')
def hello():
    return 'This is hello'

@app.route('/page')
def page():
    return '<div id="app"><div data-reactroot="" id="main"><h1>Todo list</h1><ul class="list-group"><!-- react-text: 4 --> <!-- /react-text --><li class="list-group-item "><div class="undone"><span class="glyphicon glyphicon-ok icon" aria-hidden="true"></span><!-- react-text: 8 -->learn react<!-- /react-text --><button type="button" class="close">×</button></div></li><li class="list-group-item "><div class="done"><span class="glyphicon glyphicon-ok icon" aria-hidden="true"></span><!-- react-text: 13 -->Go shopping<!-- /react-text --><button type="button" class="close">×</button></div></li><li class="list-group-item "><div class="done"><span class="glyphicon glyphicon-ok icon" aria-hidden="true"></span><!-- react-text: 18 -->buy flowers<!-- /react-text --><button type="button" class="close">×</button></div></li><!-- react-text: 20 --> <!-- /react-text --></ul><form class="form-inline"><input type="text" class="form-control" placeholder="add a new todo..."><button type="submit" class="btn btn-default">Add</button></form></div></div>'