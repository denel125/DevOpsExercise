import os

from flask import Flask
from flask import request

def create_result_file(filename):
    # create file to save result od counting
    print("create res file " + filename)
    fl = open(filename, "w+")
    fl.write("0")
    fl.close()

def write_result_file(filename):
    # save new result in the file
    res = int(read_result_file(filename)) + 1
    fl = open(filename, "w+")
    fl.write(str(res))
    fl.close()
    return res

def read_result_file(filename):
    # get result from the file
    fl = open(filename, "r")
    res = fl.read()
    fl.close()
    return res

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # counting of GET requests and  show result
    @app.route('/service', methods=["GET", "POST"])
    def counting(filename='counter.data'):
        if not os.path.isfile(filename):
            create_result_file(filename)
            
        if request.method == "GET":
            result =  read_result_file(filename)
        if request.method == "POST":
            result =  write_result_file(filename)    
             
        return 'get : ' + str(result) 
    return app


