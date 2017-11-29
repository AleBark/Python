# -*- coding: utf-8 -*-
"""
Ale Bark Bruneri
"""


class ArvoreBinaria(object):
    def __init__(self, valor=None):
        self.lLink = None
        self.rLink = None
        self.valor = valor

    def visit_root(self):
        print (self.valor)

    def insert_left(self, valor):
        self.lLink = valor

    def insert_right(self, valor):
        self.rLink = valor

    def post_order(self):
        if self.lLink is not None:
            self.lLink.post_order()

        self.visit_root()

        if self.rLink is not None:
            self.rLink.post_order()

    def pre_order(self):
        self.visit_root()

        if self.lLink is not None:
            self.lLink.pre_order()

        if self.rLink is not None:
            self.rLink.pre_order()

    def end_order(self):
        if self.lLink is not None:
            self.lLink.in_order()

        if self.rLink is not None:
            self.rLink.in_order()

        self.visit_root()


bin = ArvoreBinaria(3)
bin.insert_left(ArvoreBinaria(4))
bin.insert_right(ArvoreBinaria(5))
bin.lLink.insert_left(ArvoreBinaria(8))
bin.lLink.insert_right(ArvoreBinaria(9))
bin.rLink.insert_left(ArvoreBinaria(10))
bin.rLink.insert_right(ArvoreBinaria(11))
