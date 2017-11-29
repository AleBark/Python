# -*- coding: utf-8 -*-
"""
@author: Ale Bark Bruneri
"""


def soma(v1, v2):
    return v1 + v2

def maior_1(a, b):
    if a > b:
        return True
    else:
        return False

# igualdade de dois valores
def m_equal(a, b):
    return a == b


def m_abs(x):
    'valor absoluto de um número real'
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0

# tipos: int, bool, float, str, bytes, list


# valores são tipados
# a função type retorna o tipo de um valor:
#
# type(2)               retorna         <class 'int'>
# type('2')             retorna         <class 'str'>
# type("2222")          retorna         <class 'str'>
# type(2.)              retorna         <class 'float'>


# como verificar o tipo de um valor:
# type(valor)

# como converter um inteiro em um binário
# bin(3)

# como converter um float em inteiro
# int(3.4)

def m_test_type(valor, tipo):
    'verifica o tipo de um valor'
    if type(valor) == tipo:
        print("o tipo é: ", tipo)
    else:
        print("tipo inválido")

# m_test_type(3.0,float)
# m_test_type([1,2,3],list)
# m_test_type([1,2,3],int)


# como validar parâmetros
def maior(a, b):
    'selecionar o maior de dois números inteiros'
    if not (type(a) == int):
        print("excessão 1:", a,  "possui tipo inválido")
        return
    if not type(b) == int:
        print("excessão 2:", b,  "possui tipo inválido")
        return
    return a > b

def print_maior(a, b):
    print("o maior número é ", maior(a, b))


# exemplos de funções recursivas


def fatorial(n):
    'fatorial de um número inteiro'
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# fatorial(6)
def fibn(n):
    'retorna o fibonacci de um número inteiro'
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibn(n - 1) + fibn(n - 2)
#_______________________________________________________________


# 1) elevar um número ao quadrado
def elevar_ao_quadrado(v1):
    return v1**2

# 2) somar três números e concatenar três strings
def somar_num_strings(v1, v2, v3):
    return v1+v2+v3


# 3) multiplicar dois números inteiros, validando o tipo dos
#    parâmetros
def multiplicar_ints(v1, v2):
    if not (type(v1) == int):
        return "Primeiro parametro nao eh int"
    elif not (type(v2) == int):
        return "Segundo parametro nao eh int"
    else:
        return v1 * v2

# 4) selecionar o maior de dois números inteiros dados
def sel_maior_int(v1, v2):
    if not (type(v1) == int):
        return "Primeiro parametro nao eh int"
    elif not (type(v2) == int):
        return "Segundo parametro nao eh int"
    else:
        if v1 > v2:
            return v1
        else:
            return v2

# 5) selecionar o maior de três números
def sel_maior(v1, v2, v3):
    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v1 and v2 > v3:
        return v2
    else:
        return v3

# recursidade

# 6) calcular o produto dos naturais de 1 até um número dado
def calcular_produto_naturais(v1):
    if v1 == 0:
        return 1
    else:
        return v1 * calcular_produto_naturais(v1 - 1)
     
# 7) dado n, calcular a soma dos inteiros de 1 a n
def calcular_soma_naturais(v1):
    if v1 == 0:
        return v1
    else:
        return v1 + calcular_soma_naturais(v1-1)
        
# 8) dado n, calcular a soma de
#    1/2 + 1/4 + 1/8 + ... + 1/2^n + ...
def calcular_soma_fracoes(v1):
    if v1 == 1:
        return 0.5
    else:
        return 1 / (2**v1) + calcular_soma_fracoes(v1 - 1)
    
# 9) dado n, calcular o número e (a base dos logaritmos
#    neperianos; e = 2,718 281 828 ) até a n-ésima parcela:
#    e = 1/0! + 1/1! + 1/2! + 1/3! + ... + 1/n! + ...
def calcular_neperianos(v1):
    if v1 == 0 :
        return 1
    else:
        return (1 / calcular_produto_naturais(v1 -1)) + calcular_neperianos(v1 - 1)

# 10) sen x = x - (x^3 / 3!) + (x^5 / 5!) - (x^7 / 7!) + ...
def calcular_sen(v1,v2):
    if v1 < 2:
        return v1
    else:

        if v1 % 2:
            aux = -1
        else:
            aux = 1
            
    return calcular_sen(v1 - 1, v2) + aux * (v2 ** 2 * v1) / calcular_produto_naturais(2 * v2)
    
# 11) cos x = 1 - (x^2 / 2!) + (x^4 / 4!) - (x^6 / 6!) + ...
def calcular_cos(v1, v2):
    if v1 < 2:
        return v1
    else:

        if v1 % 2:
            aux = -1
        else:
            aux = 1
            
    return calcular_cos(v1 - 1, v2) + aux * (v2 ** 2 * v1) / calcular_produto_naturais(2 * v2)
