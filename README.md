# Gestión de Tienda de Ropa

Este proyecto es una aplicación de escritorio para la gestión de inventario de una tienda de ropa, desarrollada en Python utilizando Tkinter para la interfaz gráfica y SQLite para el almacenamiento de datos.

## Características

- Añadir nuevos productos al inventario
- Visualizar lista de productos
- Buscar productos por nombre
- Editar información de productos existentes
- Eliminar productos del inventario

## Requisitos previos

- Python 3.7 o superior
- Tkinter (generalmente viene pre-instalado con Python)
- SQLite3

## Instalación

1. Clona este repositorio:
  `git clone https://github.com/CarlosG4rc/dress_store.git`

2. Navega al directorio del proyecto:
   `cd gestion-tienda-ropa`
3. (Opcional) Crea y activa un entorno virtual:
  ```
python -m venv venv
source venv/bin/activate # En Windows usa venv\Scripts\activate
``` 
4. Instala las dependencias:
   `pip install -r requirements.txt`
   
## Uso

Para iniciar la aplicación, ejecuta:

`python main.py`

## Estructura del proyecto

```plaintext
tienda_ropa/
│
├── src/
│ ├── controllers/
│ │ └── controlador_inventario.py
│ ├── models/
│ │ └── producto.py
│ ├── views/
│ │ └── gui.py
│ └── utils/
│ └── db_manager.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Contacto

Tu Nombre - carlosesolrac93@gmail.com

Link del proyecto: [https://github.com/CarlosG4rc/dress_store](https://github.com/CarlosG4rc/dress_store)
