from flask import Flask, render_template, url_for,flash,redirect



 
app = Flask (__name__)
@app.route('/')
def index():
    return render_template('home/home.html')
@app.route('/cadastro')
def Cadastro():
    return render_template('cadastro/cadastro.html')
@app.route('/contato')
def Contato():
    return render_template('contato/contato.html')
@app.route('/login')
def Login():
    return render_template('login/login.html')
@app.route('/materiais')
def Materiais():
    return render_template('materiais/materiais.html')
@app.route('/assunto')
def Assunto():
    return render_template('assunto/assunto.html')

    

if (__name__ =='__main__'):
    app.run(debug=True)