from flask import Flask,request,render_template
from lista import Lista
app = Flask(__name__)

lista = Lista()

@app.route('/',methods = ['GET','POST'])
def root():
    global lista
    temporal = ''
    if request.method == 'POST':
        if "agregar_final" in request.form:
            valor = request.form["valor"]
            lista.append(int(valor))
            print(valor)
        if "eliminar_final" in request.form:
            temporal = lista.pop()
            print(temporal)
    return render_template('index.html',lista = lista.print(),elemento_eliminado = temporal)
if __name__ == '__main__':
    app.run(debug=True)
