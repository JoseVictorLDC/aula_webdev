from flask import Flask, render_template

app = Flask(__name__)
entradas = [
    {
        "titulo": "PRIMEIRO TEXTO DO BLOG",
        "texto": "Primeiro texto"
    },
    {
        "titulo": "SEGUNDO TEXTO DO BLOG",
        "texto": "Segundo texto"
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", posts=entradas)