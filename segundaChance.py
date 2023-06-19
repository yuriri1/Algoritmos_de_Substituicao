from collections import deque

class Clock:
    def simulador(self, tabela: list, n_quadros: int, acessos: list):
        page_fault = 0
        ponteiro = None
        fila = deque()
        

        for acesso in acessos:
            for pagina in tabela: # [pagina, bitP/A, bitR, bitM]
                if acesso == pagina[0] and pagina[1] == 0:
                    if len(fila) < n_quadros:
                        if ponteiro == None:
                            ponteiro = pagina
                        pagina[1] = 1
                        pagina[2] = 1
                        page_fault += 1
                        fila.append(pagina)
                        break
                    else:
                        while pagina[1] == 0:
                            for pag_p in fila:
                                if pag_p[2] == 1:
                                    pag_p[2] = 0
                                else:
                                    pag_p[1] = 0
                                    fila.popleft()
                                    ponteiro = fila[0]
                                    fila.append(pagina)
                                    pagina[1] = 1
                                    pagina[2] = 1
                                    page_fault += 1
                                    break
                            
                elif acesso == pagina[0] and pagina[1] == 1:
                    if pagina[2] == 0:
                        pagina[2] = 1
                        break

        return page_fault
