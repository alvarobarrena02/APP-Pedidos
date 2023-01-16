class Pedido:
    def __init__(self, id_factura, fecha_factura, cliente, producto):
        self.id_factura = id_factura
        self.fecha_factura = fecha_factura
        self.cliente = cliente
        self.producto = producto

    def infoPedido(self):
        print(f'Detalles de pedido: {self.id_factura} - {self.fecha_factura} - {self.cliente} - {self.producto}')

    def addDeseos(self):
        print('Producto añadido a la lista de deseos')

    def finalizarCompra(self):
        print('Compra finalizada')

    def pagoCompra(self):
        print('Pago realizado con éxito')

    def facturaPDF(self):
        print('Factura enviada en PDF')

    def seguimientoPedido(self):
        print('SMS enviado con el estado del pedido al cliente')