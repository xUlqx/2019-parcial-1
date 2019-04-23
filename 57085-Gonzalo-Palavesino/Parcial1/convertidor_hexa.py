def convertidor(dec):
    #Convierte el string 'dec' en un entero
    n = int(dec)
    
    #Devuelvo la conversion en hexa sin el '0x'
    num_hexa = hex(n)[2:]
    
    #Devuelvo el string en mayusculas
    result = num_hexa.upper()
    return result
   