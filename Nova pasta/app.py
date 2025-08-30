from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Usuários simulados para teste (no futuro use DB)
USUARIOS = {
    "usuario@email.com": "123456",
    "123.456.789-09": "123456"
}

@app.route("/")
def login_page():
    return render_template("index.html")

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    identity = data.get("identity")
    password = data.get("password")
    remember = data.get("remember", False)

    # Validação simples
    if not identity or not password:
        return jsonify({"message": "Campos obrigatórios"}), 400

    # Verifica se usuário existe
    if USUARIOS.get(identity) == password:
        # Aqui você poderia gerar um token JWT real
        token = "meu-token-simulado"
        return jsonify({"token": token})
    
    return jsonify({"message": "Usuário ou senha inválidos"}), 401

@app.route("/app/dashboard")
def dashboard():
    return render_template("painel.html")  # Seu painel pós-login

@app.route("/recuperar-senha")
def forgot_password():
    return "Página de recuperação de senha"

@app.route("/criar-conta")
def create_account():
    return "Página de criação de conta"

if __name__ == "__main__":
    app.run(debug=True)
