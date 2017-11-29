# -*- coding: utf-8 -*-
"""
@author: Ale Bark Bruneri
"""

class Arvore(object):
    def __init__(self, valor=None):
        self.filho = []
        self.valor = valor

    def criarFilho(self, qtde):
        for i in range(0, qtde):
            self.filho.append(Arvore())

    def setarFilhos(self, list):
        for i in range(0, len(list)):
            self.filho[i].valor = list[i]

    def mostrarValor(self):
        print self.valor

    def percorrerArvore(self):
        self.mostrarValor()
        if len(self.filho) > 0:
            for i in range(0, len(self.filho)):
                self.filho[i].percorrerArvore()
        else:
            return False


rz = Arvore(2)
rz.criarFilho(3)
rz.setarFilhos([3, 2, 1])

