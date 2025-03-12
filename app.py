from flask import Flask, render_template, request

app = Flask(__name__)

lcitas = []

@app.route("/")
def index():
    return render_template("index.html", resultado_final = None)

@app.route("/registrar_cita", methods = ["POST"])
def registrar_cita():
    try:
        cnompac = request.form["cnompac"]
        ccorpac = request.form["ccorpac"]
        ctelpac = request.form["ctelpac"]
        cespmed = request.form["cespmed"]
        dfeccit = request.form["dfeccit"]
        thorcit = request.form["thorcit"]
        csincon = request.form["csincon"]

        cita = {
            "nombre": cnompac,
            "correo": ccorpac,
            "telefono": ctelpac,
            "especialidad": cespmed,
            "fecha": dfeccit,
            "hora": thorcit,
            "sintomas": csincon
        }   
        lcitas.append(cita)
    
    except ValueError:
        resultado = "Error: entrada no válida"
    
    return render_template("index.html", citas = lcitas)

if __name__ == "__main__":
    app.run(debug = True)