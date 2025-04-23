from contacto import Contacto
from gestion_contactos import GestionContactos


class MenuContactos:
    def __init__(self):
        self.gestion_contactos = GestionContactos()

    def mostrar_menu(self):
        print('****Sistema de Contactos****')
        # Creamos el menu con un bucle while y capturamos algunos errores.
        while True:
            try:
                print('''Menu:
                1. Agregar Contacto
                2. Lista de Contactos
                3. Eliminar lista de Contactos
                4. Salir
                ''')
                # Pedimos que elija una opcion
                opcion = int(input('Porfavor elije una opcion: '))
                if opcion == 1:
                    self.agregar_contacto()
                elif opcion == 2:
                    self.lista_de_contactos()
                elif opcion == 3:
                    self.eliminar_contactos()
                elif opcion == 4:
                    print('Gracias, hasta luego')
                    break
                else:
                    print('Opcion ivalida, escoja entre las opciones del menu')


            except ValueError:
                print('Error, introduce un numero valido')
            except Exception as e:
                print(f'Ocurrio un error {e}')

    def agregar_contacto(self):
        while True:
            nombre = input('Agregar Nombre del contacto: ')
            if nombre.strip() == '':
                print('Error al agregar el nombre por favor asigne uno')
            else:
                break
        while True:
            telefono = input('Agregar numero de telefono: ')
            if telefono.strip() == '':
                print('Error al agregar el telefono por favor asigne uno')
            elif not telefono.isdigit():
                print('Error al agregar el telefono, utilize caracter numerico')
            else:
                telefono = int(telefono)
                break

        while True:
            email = input("Agregar Email:")
            if email.strip() == '':
                print('Error al agregar un email por favor asigne uno')
            elif '@' not in email:
                print('Error al agregar un email, por favor ingrese uno valido, ejemplo: nombre@email.com')
            else:
                break
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.gestion_contactos.agregar_contactos(nuevo_contacto)
        print('Contacto agregado correctamente')

    def lista_de_contactos(self):
        self.gestion_contactos.lista_contactos()

    def eliminar_contactos(self):
        self.gestion_contactos.eliminar_lista_contactos()


if __name__ == '__main__':
    app = MenuContactos()
    app.mostrar_menu()