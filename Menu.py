from Producto import *
class Menu():

    def __init__(self, lsProducto):
        self.lsObjProducto= list(lsProducto)
        self.MenuPrincipal(self.lsObjProducto)

    def MenuPrincipal(self, lsProducto):
        while True: 
            print("-----------------------------")
            print("Elija la opcion correcta:")
            print("1) Alta de producto")
            print("2) Modificacion de Producto")
            print("3) Baja de Producto")
            print("4) Fin del programa")
            option= input("Ingrese una opcion: ")
            if option == '1':
                lsProducto= self.AltaProducto(lsProducto)
            elif option == '2':
                lsProducto= self.ModificacionProducto(lsProducto)
            elif option == '3':
                lsProducto= self.BajaProducto(lsProducto)
            elif option=='4':
                print("Fin del programa.")
                break
            else:
                print("La opcion ingresada no es correcta, favor de volver a intentarlo")
        
    def AltaProducto(self, lsProducto):
        print("----------Alta de Producto---------------")
        print("Por favor ingrese los siguientes datos:")
        marca= input("Marca: ")
        modelo= input("Modelo: ")
        peso= input("Volumen/Peso: ")
        cantidad= input("Cantidad: ")

        # Armamos el objeto y agregamos a la lista
        producto= Producto(marca, modelo, peso, cantidad)
        lsProducto.append(producto)

        print("El producto se dio de alta con exito")
        return lsProducto

    def BajaProducto(self, lsProducto):
        print("----------Baja de Producto---------------")
        print("Por favor especifique que producto desea borrar")
        option=1
        for producto in lsProducto:
            print("{0}) {1} - {2} \t Peso: {3}".format(option, producto.Marca, producto.Modelo, producto.Peso))
            option+=1

        # Reutilizamos la variable option. Primero sirvio de enumerador para la lista, ahora lo usamos como selector de opcion
        option= int(input("Ingrese el numero de producto: "))
        # Borramos el objeto seleccionado: Recordar que por corchetes se le puede pasar una posicion especifica de objeto
        lsProducto.remove(lsProducto[option-1])
        print("El producto se dio de baja exitosamente.")
        return lsProducto

    def ModificacionProducto(self, lsProducto):
        print("----------Modificacion de Producto---------------")
        print("Por favor especifique que producto desea modificar")
        option=1
        for producto in lsProducto:
            print("{0}) {1} - {2} \t Peso: {3}".format(option, producto.Marca, producto.Modelo, producto.Peso))
            option+=1

        # Reutilizamos la variable option. Primero sirvio de enumerador para la lista, ahora lo usamos como selector de opcion
        option= int(input("Ingrese el numero de producto: "))
        
        print("Que atributo desea modificar: ")
        print("1) Peso")
        print("2) Cantidad")

        option2= input("Ingrese el numero de atributo: ")
        cambio= input("Ingrese el valor que desea asignar: ")
        if option2== '1':
            lsProducto[option-1].Peso = cambio
        elif option2== '2':
            lsProducto[option-1].Cantidad = cambio
        else:
            print("Eligio una opcion erronea, por favor vuelva a intentarlo.")
        
        print("El producto se modifico exitosamente.")
        return lsProducto        

