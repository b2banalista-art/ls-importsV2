from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)

# Pega do Render (Environment Variables)
EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/enviar", methods=["POST"])
def enviar():
    try:
        nome = request.form.get("nome")
        produto = request.form.get("produto")
        link = request.form.get("link")

        personalizacao = request.form.get("personalizacao")
        nome_personalizado = request.form.get("nome_personalizado")
        numero = request.form.get("numero")

        tamanho_chuteira = request.form.get("tamanho_chuteira")

        # Montar mensagem
        mensagem = f"""
        NOVO PEDIDO - LS IMPORTS

        Nome: {nome}
        Produto: {produto}
        Link: {link}
        """

        if produto == "Camisa" and personalizacao == "Sim":
            mensagem += f"""
            Personalização:
            Nome: {nome_personalizado}
            Número: {numero}
            """

        if produto == "Chuteira":
            mensagem += f"""
            Tamanho da chuteira: {tamanho_chuteira}
            """

        # Configuração do e-mail
        msg = MIMEText(mensagem)
        msg["Subject"] = "NOVO PEDIDO - LS IMPORTS"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(EMAIL, SENHA)
        servidor.sendmail(EMAIL, EMAIL, msg.as_string())
        servidor.quit()

        return render_template("sucesso.html")

    except Exception as e:
        print("ERRO:", e)
        return f"Erro interno: {e}"


if __name__ == "__main__":
    app.run(debug=True)