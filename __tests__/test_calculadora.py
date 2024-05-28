# 1 - bibliotecas, frameworks e referencias externas
import pytest
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numero, multiplicar_dois_numeros, dividir_dois_numeros
from utils.utils import ler_csv

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

def test_dividir_por_zero():
    num1 = 10
    num2 = 0
    resultado_esperado = 'Erro: Não é possível dividir por zero.'

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

# Teste Baseados em Dados = Data Driven Tests (DDT) --> Massa de Teste
    # Dados em uma lista
    # Dados em um arquivo --> vários formatos, sendo o mais comum csv, json, xml

@pytest.mark.parametrize('num1, num2, resultado_esperado', 
                         [ # array / matriz
                            (5, 7, 12), # tupla / registro
                            (0, 8, 8),
                            (10, -15, -5),
                            (6, 0.75, 6.75)    
                         ]
                        )

def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):
    # Arrange / Prepara / Configura - dados fornecidos pela massa de teste em formato de lista

    #Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('num1, num2, resultado_esperado', ler_csv('./fixtures./massa_somar.csv'))

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):
    # Arrange / Prepara / Configura - dados fornecidos pela massa de teste em formato de lista

    #Act / Executa
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido