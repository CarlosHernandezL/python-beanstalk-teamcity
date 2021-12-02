from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works from TCv2!"

@application.route("/hello")
def hello():
    return "Hello World TC!"


if __name__ == "__main__":
    application.run(port=5000, debug=True)
