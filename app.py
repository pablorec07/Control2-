from flask import Flask, jsonify, request

app = Flask(__name__)

# Repositorio temporal de datos
#Esto no representa persistencia de datos
libros = {
    101: {
        "id": 101, "titulo": "Clean code", "autor": "Robert C. Martin", "disponible": True},
    102:{
        "id": 102, "titulo": "Python Crash C", "autor": "Eric Matthes", "disponible": True},
    103:{
        "id": 103, "titulo": "Architecture patterns", "autor": "GoF", "disponible": False},
    
    }

@app.get("/")
def inicio(): 
    return jsonify(
        {
            "mensaje": "API REST de Biblioteca universitaria",
            "version": "1.0",
            "endpoints": [
                "Get /libros", #Muestra todos los libros,
                "Get /libros/<id>", #Informacion de UN libro
                "POST /libros", #Crear un nuevo libro
                "PUT /libros/<id>", #Modificar la disponibilidad
                "DELETE /libros/<id>" #borrar un libro
            ]
        }
    )

@app.get("/libros")
def obtener_Libros():
    return jsonify(list(libros.values()))

@app.get("/libros/<int:id>")
def obtener_libro(id):
    libro = libro.get(id)
    if libro:
        return jsonify(libro)
    
    return jsonify({"error": "libro no encontrado"}), 404

@app.post("/libros")
def agregar_libro():
    datos = request.get_json()
    
    
    if not datos:
        return jsonify({"error": "Debe enviar informacion"}), 400
    if "titulo" not in datos or "autor" not in datos or "disponible" not in datos:
        return jsonify({"error": "Los campos son requeridos"}), 400
    
    nuevo_id = max(libros.keys()) + 1
    
    libros[nuevo_id] ={
        "id": nuevo_id,
        "titulo": datos["titulo"],
        "autor": datos["autor"],
        "disponible": datos["disponible"]
    }
    return jsonify(libros[nuevo_id]), 201

if __name__ == "__main__":
    app.run(debug=True)