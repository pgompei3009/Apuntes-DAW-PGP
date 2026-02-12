from datetime import datetime
from dataclasses import dataclass

@dataclass
class Proveedor:
    id_proveedor = int
    nombre = str
    telefono = str
    email = str
    localidad = str

@dataclass
class Pedido:
    id_pedido = int
    fecha_pedido = datetime
    fecha_entrega = datetime
    precio_total = float
    direccion_envio = list
    peso_kg = float
    tipo_producto = str
    id_proveedor = Proveedor.id_proveedor


lista_proveedores = [
    Proveedor(1, 'Juan', '645285696', 'camionesmolan@gmail.com', 'San Clemente'),
    Proveedor(2, 'Julián', '692567154', 'vivacristorey@hotmail.es', 'Gipuzkoa')
]

lista_pedidos = [
    Pedido(101, datetime(2024,1,10), datetime(2024,1,15), 150.25, ['Av. Real 10'], 5.4, 'Textil', 1),
    Pedido(102, datetime(2024,1,11), datetime(2024,1,16), 85.00, ['Calle Mayor 5'], 1.2, 'Hogar', 2),
    Pedido(103, datetime(2024,1,12), datetime(2024,1,14), 1200.50, ['Pol. Ind. S/N'], 45.0, 'Motor', 1),
    Pedido(104, datetime(2024,1,13), datetime(2024,1,18), 45.99, ['Plaza Nueva 3'], 0.8, 'Papelería', 2),
    Pedido(105, datetime(2024,1,14), datetime(2024,1,20), 320.40, ['Calle Pez 12'], 12.3, 'Jardín', 1),
    Pedido(106, datetime(2024,1,15), datetime(2024,1,19), 210.00, ['Av. Libertad 1'], 4.5, 'Deporte', 1),
    Pedido(107, datetime(2024,1,16), datetime(2024,1,22), 65.30, ['Calle Luna 45'], 2.1, 'Mascotas', 2),
    Pedido(108, datetime(2024,1,17), datetime(2024,1,21), 890.00, ['Calle Ancha 7'], 18.0, 'Electro', 1),
    Pedido(109, datetime(2024,1,18), datetime(2024,1,25), 12.50, ['Cruceiro 4'], 0.3, 'Alimentación', 2),
    Pedido(110, datetime(2024,1,19), datetime(2024,1,24), 540.75, ['Rúa Nova 88'], 25.6, 'Construcción', 1)
]

