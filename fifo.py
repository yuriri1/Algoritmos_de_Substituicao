from collections import deque

class Fifo:
    def __init__(self):
        pass

    def simulador(self, tabela_cpy, n_quadros, acessos):
        page_fault = 0
        quadros_alocados = 0
        tabela = tabela_cpy.copy()
        fila = deque()

        for acesso in acessos:
            for pagina in tabela:
                if acesso == pagina[1] and pagina[0] == 0:
                    if quadros_alocados < n_quadros:
                        pagina[0] = 1
                        page_fault += 1
                        quadros_alocados += 1
                        fila.append(pagina)
                        break
                    else:
                        pagina_substituida = fila.popleft()
                        pagina_substituida[0] = 0
                        pagina[0] = 1
                        fila.append(pagina)
                        page_fault += 1
                        break

        return page_fault                    
