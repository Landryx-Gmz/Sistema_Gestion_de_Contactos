import os


class GestioContactos:
    def __init__(self):
        self.nombre_archivo = 'contactos.txt'

    def agregar_contactos(self, contacto):
        try:
            with open(self.nombre_archivo, 'a', encoding='utf8') as archivo:
                archivo.write(f'{contacto.nombre},{contacto.num_telef},{contacto.email}')
                print('El contacto se agrego correctamente')
        except Exception as e:
            print(f'Error al agregar contacto {e}')

    def lista_contactos(self):
        with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
            print('----Contactos----')
            archivo.read()

    def eliminar_lista_contactos(self):
        os.remove(self.nombre_archivo)
        print('Lista eliminada correctamente')
