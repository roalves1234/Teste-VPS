from flask import Flask

# Cria a aplicação Flask
app = Flask(__name__)

# Define a rota principal ("/")
@app.route("/")
def home():
    return "<h1>Olá VPS!!</h1>"

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
