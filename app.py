from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo="Flask IDGS801"
    lista=["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/operasBas", methods=['GET', 'POST'])
def operas1():
    n1=0
    n2=0
    res=0
    if request.method=='POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        res = float(n1)+float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    tem = float(n1)+float(n2)
    return f"La suma es: {tem}"

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/hola")
def hola():
    return "Hola, Mundo!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>¡Hola, {username}! Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
    </form>

    '''

if __name__ == "__main__":
    app.run(debug=True)