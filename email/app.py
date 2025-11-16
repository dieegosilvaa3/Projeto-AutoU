from flask import Flask, render_template, request, jsonify
from nlp import preparar_texto
from classificacao import classificar_email
from resposta import gerar_resposta
from utilidades import ler_arquivo

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/processar")
def processar():
    texto = request.form.get("texto_email", "")
    arquivo = request.files.get("arquivo_email")

    if arquivo and arquivo.filename:
        texto = ler_arquivo(arquivo)
    if not texto or texto.strip() == "":
        return jsonify({"error": "Nenhum conteúdo informado."}), 400

    texto_preparado = preparar_texto(texto)
    label, score, sinais = classificar_email(texto_preparado, texto_original=texto)
    resposta = gerar_resposta(label, texto_original=texto, sinais=sinais)

    return jsonify({
        "categoria": label,
        "confianca": round(score, 3),
        "resposta": resposta,
        "sinais": sinais
    })

if __name__ == "__main__":
    app.run(debug=True)