from flask import Flask

app = Flask("projeto")

@app.route("/")

def ola_mundo():
    return"Olá mundo! Esse é meu primeiro codigo flask"

app.run()
