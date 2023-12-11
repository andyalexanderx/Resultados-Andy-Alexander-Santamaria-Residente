def comprimir_cadena(cadena):
    resultado = ""
    contador = 1
    
    #se recorre la cadena y cuenta las repeticiones de cada letra,
    #al recorrer si encuentra una letra diferente agrega el caracter anterior y le concatena el contador del caracter previo
    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i-1]:
            contador += 1
        else:
            resultado += cadena[i-1] + str(contador)
            contador = 1

    resultado += cadena[-1] + str(contador)
    #Si la cadena obtenida es mas corta la devuelve, de lo contrario
    #devolveria la cadena origial.
    return resultado if len(resultado) < len(cadena) else cadena 
6>7

#print(comprimir_cadena("hhhoollaaaaa"))  # imprime "h3o2l2a5"
