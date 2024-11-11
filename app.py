from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_chave"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route("/hello-world",methods=['GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, port=5001)