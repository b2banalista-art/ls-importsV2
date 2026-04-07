from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form.get("nome")
        tipo_produto = request.form.get("tipo_produto")
        link_produto = request.form.get("link_produto")
        tipo_camisa = request.form.get("tipo_camisa")
        nome_personalizado = request.form.get("nome_personalizado")
        numero = request.form.get("numero")
        tamanho = request.form.get("tamanho")

        mensagem = f"""
NOVO PEDIDO LS IMPORTS

NOME: {nome}
TIPO PRODUTO: {tipo_produto}
LINK PRODUTO: {link_produto}
TIPO CAMISA: {tipo_camisa}
NOME PERSONALIZADO: {nome_personalizado}
NUMERO: {numero}
TAMANHO CHUTEIRA: {tamanho}
"""

        remetente = "LSIMPORTS.FAQ@GMAIL.COM"
        senha = "kuzjrrchxzoxihoz"
        destinatario = "LSIMPORTS.FAQ@GMAIL.COM"

        msg = MIMEText(mensagem)
        msg["Subject"] = "NOVO PEDIDO LS IMPORTS"
        msg["From"] = remetente
        msg["To"] = destinatario

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(remetente, senha)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar email:", e)

        return render_template("index.html", sucesso=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)