from  flask import Flask
from app.route.home import home_bp
from app.route.auth import auth_bp

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True, port=8080)