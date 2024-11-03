import tkinter as tk
from tkinter import ttk, messagebox, Scrollbar
from src.controllers.controlador_inventario import ControladorInventario

class TiendaRopaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tienda de Ropa")
        self.root.geometry("1000x600")
        
        self.controlador = ControladorInventario()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Crear pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")
        
        # Pestaña de Inventario
        self.inventario_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inventario_frame, text="Inventario")
        self.setup_inventario_tab()
        
        # # Pestaña de Ventas (para futura implementación)
        # self.ventas_frame = ttk.Frame(self.notebook)
        # self.notebook.add(self.ventas_frame, text="Ventas")
        
        # # Pestaña de Clientes (para futura implementación)
        # self.clientes_frame = ttk.Frame(self.notebook)
        # self.notebook.add(self.clientes_frame, text="Clientes")
        
    def setup_inventario_tab(self):
        # Frame para añadir productos
        add_frame = ttk.LabelFrame(self.inventario_frame, text="Añadir Producto")
        add_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        ttk.Label(add_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.nombre_entry = ttk.Entry(add_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(add_frame, text="Talla:").grid(row=1, column=0, sticky="w")
        self.talla_entry = ttk.Entry(add_frame)
        self.talla_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(add_frame, text="Color:").grid(row=2, column=0, sticky="w")
        self.color_entry = ttk.Entry(add_frame)
        self.color_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(add_frame, text="Precio:").grid(row=3, column=0, sticky="w")
        self.precio_entry = ttk.Entry(add_frame)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Label(add_frame, text="Cantidad:").grid(row=4, column=0, sticky="w")
        self.cantidad_entry = ttk.Entry(add_frame)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)
        
        ttk.Button(add_frame, text="Añadir Producto", command=self.add_product).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Frame para listar y buscar productos
        list_frame = ttk.LabelFrame(self.inventario_frame, text="Lista de Productos")
        list_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Añadir campo de búsqueda y botón
        search_frame = ttk.Frame(list_frame)
        search_frame.pack(fill="x", padx=5, pady=5)

        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))

        search_button = ttk.Button(search_frame, text="Buscar", command=self.search_products)
        search_button.pack(side="left")

        # # Añadir campo de eliminación y boton
        # delete_frame = ttk.Frame(list_frame)
        # delete_frame.pack(fill="x", padx=5, pady=5)

        # self.delete_entry = ttk.Entry(delete_frame)
        # self.delete_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # delete_button = ttk.Button(delete_frame, text="Borrar", command=self.delete_product)
        # delete_button.pack(side="left")

        ###########
        clear_button = ttk.Button(search_frame, text="Limpiar", command=self.clear_search)
        clear_button.pack(side="left", padx=(5, 0))
        
        # Crear un frame para contener el Treeview y las scrollbars
        tree_frame = ttk.Frame(list_frame)
        tree_frame.pack(expand=True, fill="both")

        # Crear Scrollbars
        y_scrollbar = Scrollbar(tree_frame, orient="vertical")
        x_scrollbar = Scrollbar(tree_frame, orient="horizontal")
        
        # Crear Treeview
        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Talla", "Color", "Precio", "Cantidad"), 
                                 show="headings", yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        
        # Configurar Scrollbars
        y_scrollbar.config(command=self.tree.yview)
        x_scrollbar.config(command=self.tree.xview)
        
        # Posicionar Treeview y Scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scrollbar.grid(row=0, column=1, sticky="ns")
        x_scrollbar.grid(row=1, column=0, sticky="ew")

        # Configurar expansión del grid
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Configurar encabezados
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Talla", text="Talla")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Cantidad", text="Cantidad")

        # Configurar anchos de columna
        for col in self.tree["columns"]:
            self.tree.column(col, width=100, minwidth=50)

        ttk.Button(list_frame, text="Actualizar Lista", command=self.update_product_list).pack(pady=10)

        # Hacer que la pestaña de inventario sea expandible
        self.inventario_frame.grid_rowconfigure(0, weight=1)
        self.inventario_frame.grid_columnconfigure(1, weight=1)

    # Añadir botones para editar y eliminar
        button_frame = ttk.Frame(list_frame)
        button_frame.pack(fill="x", padx=5, pady=5)

        edit_button = ttk.Button(button_frame, text="Editar Producto", command=self.edit_product)
        edit_button.pack(side="left", padx=(0, 5))

        delete_button = ttk.Button(button_frame, text="Eliminar Producto", command=self.delete_product)
        delete_button.pack(side="left")

        # Configurar evento de selección en el Treeview
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def on_tree_select(self, event):
        selected_items = self.tree.selection()
        if selected_items:
            self.selected_item = selected_items[0]
        else:
            self.selected_item = None

    def edit_product(self):
        if not self.selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para editar.")
            return

        # Obtener los valores actuales del producto seleccionado
        values = self.tree.item(self.selected_item)['values']
        
        # Crear una nueva ventana para editar el producto
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Producto")

        # Crear campos de entrada con los valores actuales
        ttk.Label(edit_window, text="Nombre:").grid(row=0, column=0, sticky="w")
        nombre_entry = ttk.Entry(edit_window)
        nombre_entry.insert(0, values[1])
        nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(edit_window, text="Talla:").grid(row=1, column=0, sticky="w")
        talla_entry = ttk.Entry(edit_window)
        talla_entry.insert(0, values[2])
        talla_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(edit_window, text="Color:").grid(row=2, column=0, sticky="w")
        color_entry = ttk.Entry(edit_window)
        color_entry.insert(0, values[3])
        color_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(edit_window, text="Precio:").grid(row=3, column=0, sticky="w")
        precio_entry = ttk.Entry(edit_window)
        precio_entry.insert(0, values[4])
        precio_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(edit_window, text="Cantidad:").grid(row=4, column=0, sticky="w")
        cantidad_entry = ttk.Entry(edit_window)
        cantidad_entry.insert(0, values[5])
        cantidad_entry.grid(row=4, column=1, padx=5, pady=5)

        # Función para guardar los cambios
        def save_changes():
            try:
                updated_values = {
                    'nombre': nombre_entry.get(),
                    'talla': talla_entry.get(),
                    'color': color_entry.get(),
                    'precio': float(precio_entry.get()),
                    'cantidad': int(cantidad_entry.get())
                }
                self.controlador.actualizar_producto(values[0], **updated_values)
                messagebox.showinfo("Éxito", "Producto actualizado correctamente")
                edit_window.destroy()
                self.update_product_list()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores válidos")

        # Botón para guardar cambios
        ttk.Button(edit_window, text="Guardar Cambios", command=save_changes).grid(row=5, column=0, columnspan=2, pady=10)

    def delete_product(self):
        if not self.selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este producto?"):
            values = self.tree.item(self.selected_item)['values']
            self.controlador.eliminar_producto(values[0])
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.update_product_list()
        
    def add_product(self):
        try:
            nombre = self.nombre_entry.get()
            talla = self.talla_entry.get()
            color = self.color_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            
            self.controlador.agregar_producto(nombre, talla, color, precio, cantidad)
            messagebox.showinfo("Éxito", "Producto añadido correctamente")
            self.clear_entries()
            self.update_product_list()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos")
        
    def update_product_list(self, products=None):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        productos = self.controlador.listar_productos()
        for producto in productos:
            self.tree.insert("", "end", values=producto)
    
    def search_products(self, products=None):
        try:
            nombre = self.search_entry.get()

            producto_encontrado = self.controlador.obtener_producto_nombre(nombre)
            if producto_encontrado:
                for i in self.tree.get_children():
                    self.tree.delete(i)
            else:
                messagebox.showinfo("Información", "No se encontraron productos con ese nombre")
                return
            for producto in producto_encontrado:
                self.tree.insert("", "end", values=producto)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos")
    
    # def delete_product(self, products=None):
    #     try:
    #         delete_id = self.delete_entry.get()

    #         producto_borrar = self.controlador.eliminar_producto(delete_id)
            
    #         self.update_product_list()

    #     except ValueError:
    #         messagebox.showerror("Error", "Por favor, ingrese valores válidos")
    
    def clear_search(self):
        self.clear_entries()
        self.update_product_list()
    
    def clear_entries(self):
        self.nombre_entry.delete(0, tk.END)
        self.talla_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

    
def iniciar_gui():
    root = tk.Tk()
    app = TiendaRopaGUI(root)
    root.mainloop()

__all__ = ['iniciar_gui']

if __name__ == "__main__":
    iniciar_gui()