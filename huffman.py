# -*- coding: utf-8 -*-
"""
@author: alebark
"""

from heapq import heappush, heappop, heapify


def contar_frequencias(arq):
    frequencias = {}
    with open(arq) as string:
        for linha in string:
            for char in linha:
                if char in frequencias:
                    frequencias[char] += 1
                else:
                    frequencias[char] = 1
        return frequencias


def comprimir(frequencias):
    # Cria vetor no formato PESO -> CARACTER , CODIGO
    pilha = [[peso, [caracter, ""]] for caracter, peso in frequencias.items()]

    # Ordena a pilha por ordem de peso
    heapify(pilha)

    while len(pilha) > 1:

        # Recuperando os dois elementos com menor peso
        primeiroMenorValor = heappop(pilha)
        segundoMenorValor = heappop(pilha)

        # Adicionando zeros a esquerda
        for par in primeiroMenorValor[1:]:
            par[1] = '0' + par[1]

        # Adicionando um a direita
        for par in segundoMenorValor[1:]:
            par[1] = '1' + par[1]

        # Adicionando o novo 'nó' (somatório dos menores pesos) ao array
        heappush(pilha, [primeiroMenorValor[0] + segundoMenorValor[0]] + primeiroMenorValor[1:] + segundoMenorValor[1:])

    return sorted(heappop(pilha)[1:], key=lambda p: (len(p[-1]), p))


def exibir_codigos_tabela(vetor):
    print("Caracter\tPeso\tCodigo")
    for p in vetor:
        print("%s\t%s\t%s" % (p[0]+"----------", frequencias[p[0]], p[1]))


def exibir_codigo_concatenado(huffman):
    # Caracter da string inicial = 8 bits
    # Cada 0 e 1 referenciados do carcter valem 1 bit
    codigoFinal = ''

    for posicao in huffman:
        codigoFinal = codigoFinal + posicao[1]
    return codigoFinal

def calcular_bits_originais(frequencias):
    totalbytes = 0 
    for freq in frequencias:
        totalbytes = totalbytes + frequencias[freq] * 8
    return totalbytes

def calcular_taxa_compressao(codigo, tamanhoOriginal):
    
     comprimido = len(codigo)
     taxa = 100 * comprimido / tamanhoOriginal
     print("Tamanho Original (em bytes): ",tamanhoOriginal )
     print("Tamanho após compressão (em bytes):", comprimido)
     print("Taxa de compressão:", 100 - taxa, "%")
   


caminho = "teste.txt"
frequencias = contar_frequencias(caminho)
huffman = comprimir(frequencias)
tamanhoOriginal = calcular_bits_originais(frequencias)
print("\nTabela:\n")
exibir_codigos_tabela(huffman)
print("\nCodigo concatenado: (fora de ordem)\n")
codigo_contatenado = exibir_codigo_concatenado(huffman)
print(codigo_contatenado)
print("\nTaxa de compressao:\n")
calcular_taxa_compressao(codigo_contatenado, tamanhoOriginal)
