# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome="Augusto Domiciano"
    produtos = [
    {"nome": "PlayStation 5", "preco": 2000.00},
    {"nome": "Xbox Serie X", "preco": 3999.99},
    {"nome": "Nitendo Switch", "preco": 1000.00}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200

@app.route("/livros")
def mostra_livros():
    livros = [
    {"titulo": "Duna", "autor": "Frank Hebert"},
    {"titulo": "Cosmos", "autor": "Carl Sagan"},
    {"titulo": "Os Miseraveis", "autor": "Alexandre Dumas"}]

    return render_template("livros.html", aLivros=livros), 200


app.run(debug=True)