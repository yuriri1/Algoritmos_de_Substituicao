from collections import deque
import random

class NRU:
    def __init__(self):
        pass

    def generate_lista_classes(self, lista_bit_r, lista_bit_m):
        lista=[]
        for indice,bit in enumerate(lista_bit_r):
            lista.append(lista_bit_r[indice]*2+lista_bit_m[indice])
            
        return lista

    def simulador(self, tabela, n_quadros, acessos):
        page_fault = 0
        quadros_alocados = 0
        hit = 0
        indicador = 0
        substituidos = []
        lista_bit_r = [0] * n_quadros
        lista_bit_m = [0] * n_quadros
        lista_classes = [None] * n_quadros
        cache = [None] * n_quadros
        clock_interrupt = 0  
        clock_interval = 10  

        for mem in acessos:
            if mem in cache:
                hit += 1
                index = cache.index(mem)
                lista_bit_r[index] = 1 
            else:
                if mem in substituidos:
                    index = substituidos.index(mem)
                    cache[indicador] = mem
                    lista_bit_r[indicador] = 1  
                    lista_bit_m[indicador] = 0  
                    lista_classes[indicador] = 0  
                    indicador += 1
                    page_fault += 1
                else:
                    if None in cache:
                        index = cache.index(None)
                        cache[index] = mem
                        lista_bit_r[index] = 1  
                        lista_bit_m[index] = 0  
                        lista_classes[index] = 0  
                        indicador += 1
                        page_fault += 1
                    else:
                        classes = self.generate_lista_classes(lista_bit_r, lista_bit_m)
                        min_class = min(classes)
                        min_class_indices = [i for i, c in enumerate(classes) if c == min_class]
                        lowest_class_indices = [i for i in min_class_indices if cache[i] is not None]
                        index = random.choice(lowest_class_indices)  
                        page_to_remove = cache[index]
                        cache[index] = mem
                        lista_bit_r[index] = 1  
                        lista_bit_m[index] = 0  
                        lista_classes[index] = 0  
                        indicador += 1
                        page_fault += 1
                        substituidos.append(page_to_remove)

            # Clock interrupt
            clock_interrupt += 1
            if clock_interrupt >= clock_interval:
                lista_bit_r = [0] * n_quadros  
                clock_interrupt = 0

            if indicador > n_quadros - 1:
                indicador = 0

        return page_fault

