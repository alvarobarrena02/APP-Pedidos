# POO. Entidad, clase, CLiente
#Python es un lenguaje indentado

class Cliente: #nomenclatura es PascalCase
    #constructor pide los atributos, campos, propiedades
    def __init__(self, id, nombre, email, pais, descuento):
        self.id = id #Any quiere decir que puede ser cualquier tipo de dato. Python infiere el tipo de dato. No es un tipado fuerte como Java.
        self.id = id
        self.nombre_cliente = nombre #nomenclatura es snake_case
        self.email = email
        self.pais = pais
        self.descuento = descuento

    #métodos
    def info_Cliente(self): #método de instancia permite usar atributos de clase.
        print(f'El cliente se llama {self.nombre_cliente}')
