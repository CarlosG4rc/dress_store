import sqlite3

class DBManager:
    def __init__(self, db_name='data/tienda.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                talla TEXT,
                color TEXT,
                precio REAL,
                cantidad INTEGER
            )
        ''')
    
    def insertar_producto(self, producto):
        self.cursor.execute('''
            INSERT INTO productos (nombre, talla, color, precio, cantidad)
            VALUES (?, ?, ?, ?, ?)
        ''', (producto.nombre, producto.talla, producto.color, producto.precio, producto.cantidad))
        self.conn.commit()

    def obtener_producto(self, id):
        self.cursor.execute('SELECT * FROM productos WHERE id = ?', (id,))
        return self.cursor.fetchone()
    
    def obtener_producto_nombre(self, nombre):
        self.cursor.execute('SELECT * FROM productos WHERE nombre = ?', (nombre,))
        return self.cursor.fetchall()

    def obtener_todos_productos(self):
        self.cursor.execute('SELECT * FROM productos')
        return self.cursor.fetchall()

    def actualizar_producto(self, id, **kwargs):
        set_clause = ', '.join([f"{k} = ?" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        self.cursor.execute(f'UPDATE productos SET {set_clause} WHERE id = ?', values)
        self.conn.commit()

    def eliminar_producto(self, id):
        self.cursor.execute('DELETE FROM productos WHERE id = ?', (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
