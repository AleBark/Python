# -*- coding: utf-8 -*-
"""
@author: Ale Bark Bruneri
"""


class LList:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next

    # Retornando o comprimento da lista encadeada
    def length(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.length()

    # Retornando a soma de todos os elementos da lista
    def sum_list(self):
        if self.next is None:
            return self.info
        else:
            return self.info + self.next.sum_list()

    # Retornando um vetor com todos os elementos da lista encadeada. (lista sempre tem um valor)
    def show_list(self):
        if self.next is None:
            return [self.info]
        else:
            return [self.info] + self.next.show_list()

    # Procurando valor dentro da lista encadeada
    def search(self, valor):
        if self.info == valor:
            return True
        if self.next is None:
            return False
        else:
            return self.next.search(valor)

    # Considerando que a lista encadeada sempre vai ter um elemento inicial.
    def insert_n(self, no, indice):
        if indice == 1:
            no.next = self.next
            self.next = no
        else:
            return self.next.insert_n(no, indice - 1)

    # Considerando que a lista encadeada sempre vai ter um elemento inicial.
    def remove_n(self, indice):
        if indice == 1:
            self.next = self.next.next
        else:
            return self.next.remove_n(indice - 1)
    
    #Considerando que a lista sempre tem um elemento inicial(esse pode ser acessado via update)
    def update_n(self,valor,indice):
        if indice == 0:
            self.info = valor
        else:
            self.next.update_n(valor, indice - 1)
            

l1 = LList(1, None)
l1.insert_n(LList(1, None), 1)
l1.insert_n(LList(3, None), 2)

