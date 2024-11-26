"""
charfun.py
Programa que determina si una cadena proporcionada por el usuario es palíndroma.
Para ello se preguntará por teclado al usuario tantas veces como quiera
hasta que escriba la palabra salir.

Ultima Modificación: 26/11/2024
Autor: Gregorio Coronado Morón
Dependencias: Unicodedata
"""
import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    
    Args:
        cadena (str): La cadena a verificar
        
    Returns:
        bool: True si es palíndromo, False si no lo es
        
    Raises:
        AttributeError: Si el argumento no es una cadena
    """
    # Verificar si es None o no es string
    if not isinstance(cadena, str):
        raise AttributeError("El argumento debe ser una cadena de texto")
    
    cadena = cadena.lower()
    
    # Eliminar acentos
    cadena = ''.join(c for c in unicodedata.normalize('NFD', cadena)
                    if unicodedata.category(c) != 'Mn')
    
    # Convertir a minúsculas y eliminar caracteres no alfanuméricos
    cadena_limpia = ''.join(c for c in cadena if c.isalnum())
    
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

def main():
    """Función principal que maneja la interacción con el usuario"""
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
            
        # Comprobar si es palíndromo
        try:
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")
        except AttributeError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()