from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operador = request.form["operador"]

            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                resultado = num1 / num2 if num2 != 0 else "¡No se puede dividir entre cero!"
            else:
                resultado = "Operador no válido"
        except ValueError:
            resultado = "Por favor, ingresa números válidos"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
