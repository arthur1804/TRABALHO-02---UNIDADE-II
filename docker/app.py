from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Docker! Sua aplicação está rodando com sucesso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)