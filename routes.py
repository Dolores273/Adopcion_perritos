from flask import Flask, render_template, request, redirect, url_for, flash
import database
import models

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_mensajes'


@app.route('/')
def index():
    dogs_data = database.get_available_dogs()
    
    available_dogs = []
    for row in dogs_data:
        dog_id, name, age, breed = row

        
        if breed == "Pastor Alemán":
            image_url = "https://www.hola.com/horizon/landscape/a7e539c5282d-raza-de-perro-pastor-aleman-t.jpg"
        elif breed == "Husky":
            image_url = "https://upload.wikimedia.org/wikipedia/commons/f/f5/Siberian_Husky_-_Mika.jpg"
        else:
            image_url = "https://placedog.net/400/300"

        dog_obj = models.Dog(dog_id, name, age, breed, image=image_url)
        available_dogs.append(dog_obj)
    
    return render_template('catalogo.html', dogs=available_dogs)



@app.route('/adoptar/<int:dog_id>')
def form_adopcion(dog_id):
    dog_data = database.get_dog_by_id(dog_id)
    if not dog_data:
        return "Lo sentimos, este perrito ya no está disponible.", 404

    dog_id, name, age, breed = dog_data

    if breed == "Pastor Alemán":
        image_url = "https://www.hola.com/horizon/landscape/a7e539c5282d-raza-de-perro-pastor-aleman-t.jpg"
    elif breed == "Husky":
        image_url = "https://upload.wikimedia.org/wikipedia/commons/f/f5/Siberian_Husky_-_Mika.jpg"
    else:
        image_url = "https://placedog.net/400/300"

    dog_obj = models.Dog(dog_id, name, age, breed, image=image_url)
    return render_template('confirmacion.html', dog=dog_obj)


@app.route('/historial')
def historial():
    registros = database.get_adoption_history()
    return render_template('historial.html', adopciones=registros)



@app.route('/confirmar_adopcion', methods=['POST'])
def procesar_adopcion():
    try:
        dog_id = request.form.get('dog_id')
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        address = request.form.get('address')
        id_card = request.form.get('id_card')

        dog_data = database.get_dog_by_id(dog_id)
        if not dog_data:
            return "Error: El perrito ya no está disponible.", 400

        success = database.register_adoption_transactional(
            dog_id, name, lastname, address, id_card
        )

        if success:
            return redirect(url_for('historial'))
        else:
            return "Hubo un problema técnico o el perro ya fue adoptado.", 500

    except Exception as e:
        print(f"❌ Error en el servidor: {e}")
        return "Datos de formulario inválidos.", 400


if __name__ == '__main__':
    app.run(debug=True)