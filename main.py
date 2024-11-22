# Importar
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# La tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html',size = size, lights = lights)

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# El formulario
@app.route('/form')
def form():
    return render_template('form.html')

# Resultados del formulario
@app.route('/submit', methods=['GET','POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
	
    # guardar los datos
    with open('form_data.txt', 'a') as file:
        file.write(f'Name: {name}\n')
        file.write(f'Email: {email}\n')
        file.write(f'Address: {address}\n')
        file.write(f'Date: {date}\n')
        file.write('-------------------------\n')
 
 
    return render_template('form_result.html', name=name, email=email, date = date, address = address)

app.run(debug=True)
