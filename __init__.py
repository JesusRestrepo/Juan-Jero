from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/raza-gyrolandas')
def razas():
    return render_template('gyrolandas.html')

@app.route('/raza-gyrolandas/pagina-2')
def raza2():
    return render_template('segunda.html')

@app.route('/raza-gyrolandas/pagina-3')
def raza3():
    return render_template('tercera.html')

@app.route('/sobre-nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html')