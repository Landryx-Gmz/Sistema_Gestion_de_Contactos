class Contacto:
    contador_id = 0

    def __init__(self, nombre=str, num_telef=int, email=str):
        Contacto.contador_id += 1
        self.id_contacto = Contacto.contador_id
        self.nombre = nombre
        self.num_telef = num_telef
        self.email = email

    def __str__(self):
        return f'Id: {self.id_contacto}, Nombre: {self.nombre}, Telefono: {self.num_telef}, Email: {self.email}'
