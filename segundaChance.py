from collections import deque

class Clock:
    def __init__(self):
        pass

    def simulador(self, tabela_cpy, n_quadros, acessos):
        page_fault = 0
        cache = [None] * n_quadros
        indices_cache = [0] * n_quadros
        indicador = 0

        for mem in acessos:
            if mem in cache:
                indices_cache[cache.index(mem)] = 1
            else:
                if None in cache:
                    indicador_cache = cache.index(None)
                    cache[indicador_cache] = mem
                    indices_cache[indicador_cache] = 1
                    page_fault += 1
                    indicador = (indicador + 1) % n_quadros
                else:
                    while True:
                        if indices_cache[indicador] == 0:
                            cache[indicador] = mem
                            indices_cache[indicador] = 1
                            page_fault += 1
                            indicador = (indicador + 1) % n_quadros
                            break
                        else:
                            indices_cache[indicador] = 0
                            indicador = (indicador + 1) % n_quadros

        return page_fault
