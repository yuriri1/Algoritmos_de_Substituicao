from gerador import Gerador
from fifo import Fifo
from lru import LRU

def main():
    gerador = Gerador()
    n_quadros, total_paginas = entrada()
    n_acessos = 256
    fifo = Fifo()
    lru = LRU()

    tabela = gerador.gera_tabela_paginas(total_paginas)
    acessos = gerador.gera_acessos(total_paginas, n_acessos)

    tabela_fifo = [linha[:] for linha in tabela]
    tabela_lru = [linha[:] for linha in tabela]

    print("Em uma sequencia de ", n_acessos, " acessos, com ", total_paginas, " páginas distintas e ", n_quadros, " quadros, temos:")
    print("Fifo: ", fifo.simulador(tabela_fifo, n_quadros, acessos), " page faults")
    print("LRU: ", lru.simulador(tabela_lru, n_quadros, acessos), " page faults")



def entrada():
    print("Algoritmos de Substituição de Páginas")
    n_quadros = int(input("Digite o número de quadros: "))
    total_paginas = int(input("Digite o número total de páginas distintas: "))

    return n_quadros, total_paginas


if __name__ == "__main__":
    main()