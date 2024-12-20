from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_chave"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
login_menager = LoginManager()

db.init_app(app)
login_menager.init_app(app)

login_menager.login_view = 'login'

@login_menager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        user = User.query.filter_by(username=username).first()
        print("ffffffffffffffffffffffff",user)
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated )
            return jsonify({"Mensagem": "Autenticação Realizada com Sucesso!"})
    else:
        return jsonify({"Mensagem": "Credencial Inválida"}), 400

@app.route("/login",methods=['GET'])
def get_login():
    data = request.json
    
    return jsonify(data), 200  
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)