from flask import Flask
import time

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
@make_bold
def hello_world():
    # nw()
    return '<p>Hello, Worldsss!</p>' \
    '<p>Hello again</p>'

# @decorator_function
# def nw():
#     return '<p>bye</p>'


if __name__ == "__main__":
    app.run()


