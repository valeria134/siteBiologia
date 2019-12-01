from flask import Flask, render_template
from formulario import CadastroForm

 
app = Flask (__name__)
app.config['SECRET_KEY'] = 'dkshvfdikhgolfhvljh'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=["GET", "POST"])
def Cadastro():
    formulario=CadastroForm()
    return render_template(
        'cadastro.html',
        formulario=formulario
        )


@app.route('/login')
def Login():
    return render_template('login.html')    

if (__name__ =='__main__'):
    app.run(debug=True, port = 5001)