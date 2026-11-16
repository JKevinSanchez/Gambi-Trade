class ActivoFinanciero:
    """Representa una criptomoneda del portafolio del usuario.

    Guarda los datos básicos del activo (nombre, símbolo, cantidad y precio)
    y valida los valores cuando se modifican mediante los setters.
    """

    def __init__(self, id, nombre, simbolo, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._simbolo = simbolo
        self._cantidad = cantidad
        self._precio = precio

    # ---------- Getters ----------
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_simbolo(self):
        return self._simbolo

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # ---------- Setters (con validación) ----------
    def set_nombre(self, nombre):
        """Cambia el nombre. Lanza ValueError si está vacío."""
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre

    def set_simbolo(self, simbolo):
        """Cambia el símbolo (siempre en mayúsculas). Lanza ValueError si está vacío."""
        if simbolo.strip() == "":
            raise ValueError("El símbolo no puede estar vacío")
        self._simbolo = simbolo.upper()

    def set_cantidad(self, cantidad):
        """Cambia la cantidad. Lanza ValueError si es negativa."""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = cantidad

    def set_precio(self, precio):
        """Cambia el precio. Lanza ValueError si es negativo."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    # ---------- Métodos auxiliares ----------
    def calcular_valor_total(self):
        """Devuelve lo que vale esta posición (cantidad por precio)."""
        return self._cantidad * self._precio

    def a_diccionario(self):
        """Convierte el objeto en diccionario para poder guardarlo en la session."""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "simbolo": self._simbolo,
            "cantidad": self._cantidad,
            "precio": self._precio
        }


def crear_desde_diccionario(datos):
    """Reconstruye un ActivoFinanciero a partir de un diccionario de la session."""
    return ActivoFinanciero(
        datos["id"],
        datos["nombre"],
        datos["simbolo"],
        datos["cantidad"],
        datos["precio"]
    )