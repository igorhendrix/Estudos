from flask import Flask, render_template, request

app = Flask(__name__)


def criar_retangulo(lado, altura, simbolo):
    return "\n".join(simbolo * lado for _ in range(altura))


@app.route("/", methods=["GET", "POST"])
def pagina_inicial():
    retangulo = None
    erro = None

    if request.method == "POST":
        try:
            lado = int(request.form["lado"])
            altura = int(request.form["altura"])
            simbolo = request.form["simbolo"].strip()

            if lado < 1 or altura < 1 or not simbolo:
                erro = "Informe valores positivos e um símbolo."
            else:
                retangulo = criar_retangulo(lado, altura, simbolo)
        except (KeyError, ValueError):
            erro = "Preencha todos os campos corretamente."

    return render_template("index.html", retangulo=retangulo, erro=erro)


if __name__ == "__main__":
    lado = int(input("Quantas colunas: "))
    altura = int(input("Quanto de altura: "))
    simbolo = input("Qual será o simbolo: ")
    print(criar_retangulo(lado, altura, simbolo))

