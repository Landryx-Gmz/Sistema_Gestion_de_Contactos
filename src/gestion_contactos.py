import os

from contacto import Contacto


class GestionContactos:
    def __init__(self):
        self.contacto = Contacto
        self.nombre_archivo = 'contactos.txt'

    def agregar_contactos(self, contacto):
        try:
            with open(self.nombre_archivo, 'a', encoding='utf8') as archivo:
                archivo.write(
                    f'ID: {contacto.id_contacto}\n Nombre: {contacto.nombre}\n Telefono: {contacto.num_telef}\n Email: {contacto.email}\n')
                print('El contacto se agrego correctamente')
        except Exception as e:
            print(f'Error al agregar contacto {e}')

    def lista_contactos(self):
        try:
            with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
                print('----Contactos----')
                print(archivo.read())
        except FileNotFoundError:
            print("No hay contactos para mostrar.")
        except Exception as e:
            print(f'Ocurrio un error al leer el archivo: {e}')

    def eliminar_lista_contactos(self):
        os.remove(self.nombre_archivo)
        print('Lista eliminada correctamente')
