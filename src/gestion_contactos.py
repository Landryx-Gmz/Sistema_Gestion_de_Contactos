class GestioContactos:
    def __init__(self):
        self.nombre_archivo = 'contactos.txt'

    def agregar_contactos(self, contacto):
        with open(self.nombre_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{contacto.nombre},{contacto.num_telef},{contacto.email}')
