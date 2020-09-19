from flask import Flask, render_template,request
from formulario import Formulario


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    formulario_usuario = Formulario(request.form)

    if request.method == 'POST':
        print(formulario_usuario.usuario.data)
        print(formulario_usuario.correo.data)
        print(formulario_usuario.comentario.data)

    return render_template('formulario.html',bootraplink = 'https://getbootstrap.com/',title= "formulario", form = formulario_usuario)


@app.route('/nombre')
def nombre():
    mi_nombre = request.args.get('nombre','ricardo')
    return "hola {}".format(mi_nombre)

@app.route('/calculadora')
def calculadora():
    operacion = request.args.get("operacion")
    n1 = int(request.args.get("n1"))
    n2 = int(request.args.get("n2"))

    if operacion == "suma":
        resultado = n1 + n2
        operacion_nombre = "Suma"

    elif operacion == "resta":
        resultado = n1 - n2
        operacion_nombre = "Resta"
    
    elif operacion == "multiplicacion":
        resultado = n1 * n2
        operacion_nombre = "Multiplicacion"
    
    elif operacion == "division":
        resultado = n1 // n2
        operacion_nombre = "Division"
    
    elif operacion == "modulo":
        resultado = n1 % n2
        operacion_nombre = "Modulo"

    return render_template('calculadora.html',bootraplink = 'https://getbootstrap.com/',resultado= resultado, n1 = n1 , n2 = n2 , operacion = operacion_nombre)

@app.route('/parametros')
@app.route('/parametros/<nombre>')
def paramse(nombre="ricardo"):
    return "hola {}".format(nombre)

@app.route('/calculadora/<int:n1>+<int:n2>')
@app.route('/calculadora/<int:n1>sum<int:n2>')
@app.route('/calculadora/<int:n1>suma<int:n2>')
def calculadora_suma(n1=0,n2=0):
    resultado = n1 + n2
    return render_template('calculadora.html',bootraplink = 'https://getbootstrap.com/',resultado= resultado, n1 = n1 , n2 = n2 , operacion = "suma")

@app.route('/calculadora/<int:n1>*<int:n2>')
@app.route('/calculadora/<int:n1>multi<int:n2>')
@app.route('/calculadora/<int:n1>multiplicacion<int:n2>')
def calculadora_multiplicacion(n1=0,n2=0):
    resultado = n1 * n2
    return render_template('calculadora.html',bootraplink = 'https://getbootstrap.com/',resultado= resultado, n1 = n1 , n2 = n2 , operacion = "multiplicacion")


@app.route('/calculadora/<int:n1>-<int:n2>')
@app.route('/calculadora/<int:n1>res<int:n2>')
@app.route('/calculadora/<int:n1>resta<int:n2>')
def calculadora_resta(n1=0,n2=0):
    resultado = n1 - n2
    return render_template('calculadora.html',bootraplink = 'https://getbootstrap.com/',resultado= resultado, n1 = n1 , n2 = n2 , operacion = "resta")

@app.route('/calculadora/<int:n1>/<int:n2>')
@app.route('/calculadora/<int:n1>div<int:n2>')
@app.route('/calculadora/<int:n1>division<int:n2>')
def calculadora_division(n1=0,n2=0):
    resultado = n1 // n2
    return render_template('calculadora.html',bootraplink = 'https://getbootstrap.com/',resultado= resultado, n1 = n1 , n2 = n2 , operacion = "division")

if __name__ == '__main__':
    app.run(debug=True)