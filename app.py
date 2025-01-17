from flask import Flask
from view import views

app = Flask(__name__)

app.register_blueprint(views, urlprefix="/views")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
