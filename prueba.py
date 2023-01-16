from datetime import datetime
# Importar las clases de los ficheros anteriormente creados (Cliente, Producto y Pedido)
from Cliente import Cliente
from Pedidos import Pedido
from Producto import Producto


def registrar_cliente(): #Método que registra un cliente
    cliente1 = Cliente(1, 'Juan', 'juan@gmail.com', 'Francia', True)
    cliente1.info_Cliente()

def registrar_producto(): #Método que registra un producto
    producto1 = Producto(10, 'Zapatillas', 15, 49.99, datetime.now())
    producto1.ficha_Producto()

def registrar_pedido(): #Método que registra un pedido
    cliente100 = Cliente(100, 'Maria', 'maria@gmail.com', 'Italia', False) #Instanciar un objeto de la clase Cliente
    producto100 = Producto(100, 'Bufanda', 5, 9.95, datetime.now()) #Instanciar un objeto de la clase Producto

    #pedido0 = Pedidos(100, datetime.now(), 1, 2) #Python tipado dinámico. Cliente es un number... ok
    
    pedido1 = Pedido(101, datetime.now(), cliente100.nombre_cliente, producto100.nombre_producto) #Se crea un pedido con los datos del cliente y del producto que se han creado anteriormente en las variables cliente100 y producto100 respectivamente

    pedido1.infoPedido() #Muestra los detalles del pedido
    pedido1.addDeseos() #Añade el producto a la lista de deseos
    pedido1.finalizarCompra() #Finaliza la compra
    pedido1.pagoCompra() #Realiza el pago
    pedido1.facturaPDF() #Envía la factura en PDF
    pedido1.seguimientoPedido() #Envía un SMS con el estado del pedido al cliente

registrar_cliente()
registrar_producto()
registrar_pedido()
