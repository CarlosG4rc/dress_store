from src.models.producto import Producto
from src.utils.db_manager import DBManager

class ControladorInventario:
    def __init__(self):
        self.db_manager = DBManager()

    def agregar_producto(self, nombre, talla, color, precio, cantidad):
        producto = Producto(None, nombre, talla, color, precio, cantidad)
        self.db_manager.insertar_producto(producto)

    def obtener_producto(self, id):
        return self.db_manager.obtener_producto(id)
    
    def obtener_producto_nombre(self, nombre):
        return self.db_manager.obtener_producto_nombre(nombre)

    def actualizar_producto(self, id, **kwargs):
        self.db_manager.actualizar_producto(id, **kwargs)

    def eliminar_producto(self, id):
        self.db_manager.eliminar_producto(id)

    def listar_productos(self):
        return self.db_manager.obtener_todos_productos()