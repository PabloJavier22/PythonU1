def esPalindromo(cadena):
    if not cadena:
        return False
    cadenaFormateada = ''.join(c.lower() for c in cadena if c.isalnum())
    return cadenaFormateada == cadenaFormateada[::-1]

if __name__ == "__main__":
    cadena = input("Introduce la frase para comprobar si es palíndroma: ")
    if esPalindromo(cadena):
        print(f'"{cadena}" es un palíndromo.')
    else:
        if cadena == "":
            print("No has introducido ninguna frase.")
        else:
            print(f'"{cadena}" no es un palíndromo.')
