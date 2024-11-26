"""
Suite de pruebas unitarias para la función esPalindromo del módulo charfun.py

Autor: Adrian Vitys Vitiene
Fecha: 26/11/2024
"""

import unittest
from app.scripts.charfun import esPalindromo

class TestPalindromo(unittest.TestCase):
    def test_palindromos_simples(self):
        """Prueba palíndromos básicos sin espacios ni caracteres especiales"""
        self.assertTrue(esPalindromo("oso"))
        self.assertTrue(esPalindromo("radar"))
        self.assertTrue(esPalindromo("somos"))
        self.assertFalse(esPalindromo("hola"))
        self.assertFalse(esPalindromo("python"))

    def test_palindromos_con_espacios(self):
        """Prueba palíndromos que contienen espacios"""
        self.assertTrue(esPalindromo("anita lava la tina"))
        self.assertTrue(esPalindromo("a man a plan a canal panama"))
        self.assertTrue(esPalindromo("never odd or even"))
        self.assertFalse(esPalindromo("esto no es un palindromo"))

    def test_palindromos_con_mayusculas(self):
        """Prueba palíndromos con mezcla de mayúsculas y minúsculas"""
        self.assertTrue(esPalindromo("Anita Lava La Tina"))
        self.assertTrue(esPalindromo("AmOr a RoMa"))
        self.assertTrue(esPalindromo("SOMOS"))

    def test_palindromos_con_tildes(self):
        """Prueba palíndromos con caracteres acentuados"""
        self.assertFalse(esPalindromo("átará"))
        self.assertTrue(esPalindromo("ánita lava la tiná"))
        self.assertFalse(esPalindromo("él ve que leveé"))

    def test_palindromos_con_puntuacion(self):
        """Prueba palíndromos con signos de puntuación"""
        self.assertTrue(esPalindromo("¿Somos o no somos?"))
        self.assertTrue(esPalindromo("¡Anita, lava la tina!"))
        self.assertTrue(esPalindromo("A man, a plan, a canal: Panama"))

    def test_casos_especiales(self):
        """Prueba casos límite y especiales"""
        self.assertTrue(esPalindromo(""))
        self.assertTrue(esPalindromo("a"))
        self.assertTrue(esPalindromo("  "))
        self.assertTrue(esPalindromo(".,;"))

    def test_casos_invalidos(self):
        """Prueba casos con tipos de datos inválidos"""
        with self.assertRaises(AttributeError):
            esPalindromo(None)
        with self.assertRaises(AttributeError):
            esPalindromo(123)
        with self.assertRaises(AttributeError):
            esPalindromo(['lista'])

if __name__ == '__main__':
    unittest.main()