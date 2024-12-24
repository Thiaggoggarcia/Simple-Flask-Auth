from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

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
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"Mensagem": "Autenticacao Realizada com Sucesso!"})
        else:
            return jsonify({"Mensagem":"Usuario ou Senha incorreto!"}), 400
    else:
        return jsonify({"Mensagem": "Credencial Invalida"}), 400
    
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"Mensagem":"Logout Realizado com Sucesso!"})
      
@app.route("/user", methods=['POST'])
@login_required # Caso habilitado será permitido apenas o cadastro por pessoas já autênticadas no sistema      
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"Mensagem":"Usuario Criado Com Sucesso!"})
    
    return jsonify({"Mensagem":"Erro ao Cadastrar Usuario!"}), 400 
    
@app.route("/view_user", methods=['GET'])
def view_user():
    data = request.json
    username = data.get('username')
    
    if username:
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({
                "username": user.username,
                "password":user.password
                })
        return jsonify({"Mensagem": "Usuario nao encontrado!"}), 401
    
    return jsonify({"Mensagem": "Usuario nao encontrado!"}), 401
    
@app.route("/delete_user", methods=['DELETE'])
@login_required
def delete_user():
    data = request.json
    username = data.get('username')
    
    if username:
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"Mensagem":"Usuario Deletado Com Sucesso!"})
        
        return jsonify({"Mensagem":"Usuario Nao Localizado!"}), 400 
    
@app.route("/update_user", methods=['PUT'])
@login_required
def update():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user:
            user.username = username
            user.password = password
            db.session.commit()
            return jsonify({"Mensagem":"Usuario Atualizado com Sucesso!"})
        
        return jsonify({"Mensagem":"Usuario nao localizado"}), 401
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)