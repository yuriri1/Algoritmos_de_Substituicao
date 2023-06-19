import random

class Gerador:
    def gera_acessos(self, paginas_distintas: int, n_acessos: int):
        return [random.randint(1, paginas_distintas) for i in range(n_acessos)]
    
    def gera_tabela_paginas(self, paginas_distintas: int):
        tabela_paginas = []
        for i in range(1, paginas_distintas+1):
            tabela_paginas.append([i, 0, 0, 0])  # [pagina, bitP/A, bitR, bitM]

        return tabela_paginas
    