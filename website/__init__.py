from flask import Flask


def create_app():
    app = Flask(__name__)
    # This is the secret key, do not share, just a random string i made up
    app.config['SECRET_KEY'] = 'oiuhsd2fjeruyto80wp4qnf66mdcn'
    return app
