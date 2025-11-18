from flask import Flask
from routes.measurements import measurements_bp

app = Flask(__name__)

# Registrar rotas
app.register_blueprint(measurements_bp, url_prefix="/measurements")

@app.route("/")
def home():
    return {"status": "ok", "message": "Babysense API funcionando"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000) 
