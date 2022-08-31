# notes:
# when you put this __init__.py file inside of a folder, it makes it a package...
#   therefore: the website folder is a python package and can be imported in main.py
#       like this [inside main.py]:
#           ...
#           from website import create_app
#           ...

from flask import Flask


def create_app():
    app = Flask(__name__)
    # This is the secret key, do not share, just a random string i made up
    app.config['SECRET_KEY'] = 'oiuhsd2fjeruyto80wp4qnf66mdcn'
    return app
