from collections import deque

class Fifo:
    def simulador(self, tabela: list, n_quadros: int, acessos: list):
        page_fault = 0
        quadros = deque()

        for acesso in acessos:
            for pagina in tabela: # [pagina, bitP/A, bitR, bitM]
                if acesso == pagina[0] and pagina[1] == 0:
                    if len(quadros) < n_quadros:
                        pagina[1] = 1
                        page_fault += 1
                        quadros.append(pagina)
                        break
                    else:
                        pagina_substituida = quadros.popleft()
                        pagina_substituida[1] = 0
                        pagina[1] = 1
                        quadros.append(pagina)
                        page_fault += 1
                        break

        return page_fault                    
