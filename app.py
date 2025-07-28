from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
import random
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class NumeroAleatorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(6), unique=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<NumeroAleatorio {self.numero}>'

@app.route('/')
def index():
    # Buscar todos os números ordenados pelo mais recente
    numeros = NumeroAleatorio.query.order_by(NumeroAleatorio.data_criacao.desc()).all()
    return render_template('index.html', numeros=numeros)

@app.route('/gerar')
def gerar_numero():
    while True:
        novo_numero = str(random.randint(100000, 999999))
        # Verificar se o número já existe no banco
        if not NumeroAleatorio.query.filter_by(numero=novo_numero).first():
            break
    
    # Salvar no banco
    novo_registro = NumeroAleatorio(numero=novo_numero)
    db.session.add(novo_registro)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Verifica se estamos em ambiente de produção
    if os.environ.get('ENV') == 'production':
        from waitress import serve
        serve(app, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        app.run(debug=True)