class Producto:
    def __init__(self, id, nombre, talla, color, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.talla = talla
        self.color = color
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
    
    def __str__(self):
        return f'{self.nombre} -Talla: {self.talla}, Color: {self.color}, Precio: ${self.precio}, Stock {self.cantidad}'