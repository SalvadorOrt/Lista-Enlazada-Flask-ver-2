from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def root():
    if request.method == 'POST':
        if "agregar_final" in request.form:
            valor = request.form["valor"]
            print(valor)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
