import random

class Gerador:
    def __init__(self):
        pass
    
    def gera_acessos(self, paginas_distintas, n_acessos):
        return [random.randint(0, paginas_distintas-1) for i in range(n_acessos)]
    
    def gera_tabela_paginas(self, paginas_distintas):
        tabela_paginas = []
        for i in range(paginas_distintas):
            tabela_paginas.append([0, i])

        return tabela_paginas
    