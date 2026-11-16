from flask import Flask, session
from modelos import ActivoFinanciero, crear_desde_diccionario

app = Flask(__name__)

# Necesaria para que Flask pueda firmar la cookie de la session
app.secret_key = "clave_secreta_del_proyecto"


# ---------- Funciones auxiliares ----------

def obtener_activos():
    """Devuelve la lista de criptos guardadas en la session como objetos.

    Si todavía no hay ninguna, crea la lista vacía.
    """
    lista_objetos = []

    if "activos" not in session:
        session["activos"] = []

    for datos in session["activos"]:
        lista_objetos.append(crear_desde_diccionario(datos))

    return lista_objetos


def guardar_activos(lista_objetos):
    """Guarda la lista de objetos en la session.

    La session solo admite datos simples, así que se pasan a diccionarios.
    """
    lista_diccionarios = []

    for activo in lista_objetos:
        lista_diccionarios.append(activo.a_diccionario())

    session["activos"] = lista_diccionarios


# ---------- Rutas ----------

@app.route("/")
def index():
    """Ruta principal. De momento es una prueba; luego mostrará index.html."""
    activos = obtener_activos()
    return "Funciona. Criptos guardadas: " + str(len(activos))


if __name__ == "__main__":
    app.run(debug=True)