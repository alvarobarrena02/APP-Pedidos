class Producto: #nomenclatura es PascalCase
    #constructor pide los atributos, campos, propiedades
    def __init__(self, id, nombre, unidades, precio, fecha_alta):
        self.id = id
        self.nombre_producto = nombre
        self.unidades = unidades
        self.precio = precio
        self.fecha_alta = fecha_alta

    def ficha_Producto(self):
        print(f'Los datos del producto son: \nNombre: {self.nombre_producto}\nUnidades: {self.unidades}\nPrecio: {self.precio}€\nFecha de alta: {self.fecha_alta}')