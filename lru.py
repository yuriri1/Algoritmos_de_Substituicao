from collections import deque

class LRU:
    def simulador(self, tabela: list, n_quadros: int, acessos: int):
        page_fault = 0
        fila = deque()

        for acesso in acessos:
            for pagina in tabela:
                if acesso == pagina[0] and pagina[1] == 0:
                    if len(fila) < n_quadros:
                        pagina[1] = 1
                        page_fault += 1
                        fila.append(pagina)
                        break
                    else:
                        pagina_substituida = fila.popleft()
                        pagina_substituida[1] = 0
                        pagina[1] = 1
                        fila.append(pagina)
                        page_fault += 1
                        break
                elif acesso == pagina[0] and pagina[1] == 1:
                    fila.remove(pagina)
                    fila.append(pagina)
                    break

        return page_fault
