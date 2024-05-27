# 1 - bibliotecas, frameworks e referencias externas
import pytest
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numero, multiplicar_dois_numeros, dividir_dois_numeros

# 2 - Testes

def test_somar_dois_numeros():

    # Padrão / Standard AAA (se diz Triple A / 3A) = Arrange, Act, Assert

    # Arrange / Prepara / Configura
    # Dados de entrada e saida
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    #Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():
    num1 = 10
    num2 = 4
    resultado_esperado = 6

    resultado_obtido = subtrair_dois_numero(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():
    num1 = 3
    num2 = 5
    resultado_esperado = 15

    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    num1 = 10
    num2 = 2
    resultado_esperado = 5

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido