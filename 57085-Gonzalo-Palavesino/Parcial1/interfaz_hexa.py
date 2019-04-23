from convertidor_hexa import convertidor

def main():
    while (True):
        x = input("Ingrese un numero a convertir: ")
        y = int(x)
        if (type(y) == int): 
            print("La conversion a hexa del numero ingresado es: ", convertidor(y))
            break
      
            
         


def interfaz_hexa(val):
    try:
        nro = int(val)
        if (type(nro) != int):
            return "Error, el valor ingresado no es un numero"
        else:
            return convertidor(nro)
    except ValueError:
        return "Error, el valor ingresado no es un numero"

        

main()  