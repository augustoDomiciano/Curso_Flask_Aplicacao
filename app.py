# coding: utf-8
from flask import Flask, render_template, request, redirect,url_for
app = Flask("projeto")

#Rota raiz do projeto
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome="Entrar"
    produtos = [
    {"Categoria": "Livros", "Quantidade": 200},
    {"Categoria": "Games", "Quantidade": 500},
    {"Categoria": "Moda", "Quantidade": 100}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200

#Rota da pagina de livros
@app.route("/livros")
def mostra_livros():
    livros = [
    {"titulo": "Duna", "autor": "Frank Hebert"},
    {"titulo": "Cosmos", "autor": "Carl Sagan"},
    {"titulo": "Os Miseraveis", "autor": "Alexandre Dumas"}]

    return render_template("livros.html", aLivros=livros), 200

#Rota da pagina de games
@app.route("/games")
def mostra_games():
    games = [
    {"nome": "PRODUTO", "preco": "PREÇO"},
    {"nome": "PlayStation 5", "preco": 2000.00},
    {"nome": "Xbox Serie X", "preco": 3999.99},
    {"nome": "Nitendo Switch", "preco": 1000.00}]

    return render_template("games.html", aGames=games), 200

#Rota de login do usuario
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Cadastro incorreto. Por favor, tente novamente mais tarde'
        else:
            return redirect(url_for('mostra_livros'))
    return render_template('login.html', error=error)

#Nova rota teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
    return "Nova rota teste<br>Variável: {}".format(variavel), 200

app.run()



app.run(debug=True)