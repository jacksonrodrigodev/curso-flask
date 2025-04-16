from flask import request, make_response, jsonify
from database.db import db
from main import app
from models import Jogos


@app.route("/")
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return make_response(jsonify([jogo.jogo_to_dict() for jogo in lista]), 200)


@app.route(
    "/criar",
    methods=[
        "POST",
    ],
)
def criar():
    data = request.get_json()

    nome = data.get("nome")
    categoria = data.get("categoria")
    console = data.get("console")

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        return make_response(jsonify({"error": "Jogo já existe!"}), 400)

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    return make_response(jsonify(novo_jogo.jogo_to_dict()), 201)


@app.route(
    "/atualizar/<int:id>",
    methods=[
        "PATCH",
    ],
)
def atualizar(id):
    data = request.get_json()

    jogo = Jogos.query.get_or_404(id)
    jogo.nome = data.get("nome")
    jogo.categoria = data.get("categoria")
    jogo.console = data.get("console")

    db.session.add(jogo)
    db.session.commit()

    return make_response(jsonify(jogo.jogo_to_dict()), 200)


@app.route(
    "/deletar/<int:id>",
    methods=[
        "DELETE",
    ],
)
def deletar(id):

    jogo = Jogos.query.get_or_404(id)
    db.session.delete(jogo)
    db.session.commit()
    return make_response(jsonify({"message": "Jogo deletado com sucesso!"}), 200)
