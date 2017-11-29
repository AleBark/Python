# -*- coding: utf-8 -*-
"""
@author: Ale Bark Bruneri
"""

# Métodos de lista

# first/head 
# rest/tail 
# search 
# show_info
# length
# insert_n
# update_n
# remove_n
# show_list

# remove_left
# remove_right
# insert_left 
# insert_right 
# void

l0 = [1]
l1 = [7, 5, 0, -2, 4]
l2 = ["manga", "abacate", "laranja"]
l3 = [["Maria", "maria@gmail.com", 987651318], ["Nicolau", "nicky@yahoo.com", 912347367],
      ["Bob", "bbg2@gmail.com", 998078734]]


def first(lst):
    return [lst[0]]

def rest(lst):
    return lst[1:]

def lenght(l1):
    if not rest(l1):
        return 0
    else:
        return 1 + lenght(rest(l1))

def search(l1, v1):
    if l1:
        if first(l1) == v1:
            return True
        elif not rest(l1):
            return False
        else:
            return search(rest(l1), v1)
    else:
        return False

def search_pos(l1, v1):
    if search(l1, v1):
        if first(l1) == v1:
            return 0
        else:
            return 1 + search_pos(rest(l1), v1)
    else:
        return -1

def show_list(lst):
    if list:
        return first(lst) + show_list(rest(lst))

def update_n(lista, valor, posicao):
    if posicao == 0:
        return [valor] + rest(lista)
    else:
       return first(lista) + update_n(rest(lista), valor , posicao - 1)
        
def remove_n(lista, valor, posicao):
    if posicao == 0:
        return rest(lista)
    else:
        return first(lista) + remove_n(rest(lista), valor, posicao - 1)
 
    
def insert_n(lista, valor, posicao):
    if posicao == 0:
            return [valor] + lista
    else:
        return first(lista) + insert_n(rest(lista), valor , posicao - 1)
    

def show_info(lista, posicao):
    if posicao == 0:
            return lista[posicao]
    else:
        return show_info(rest(lista), posicao - 1)