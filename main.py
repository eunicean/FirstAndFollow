from collections import defaultdict

EPSILON = 'ε'
ENDMARKER = '$'

class Gramatica():
    def __init__(self):
        self.producciones = defaultdict(list)
        self.no_terminales = set()
        self.terminales = set()
        self.simbolo_inicial = None

    def agregar_produccion(self, var_prod, lista_producciones):
        if self.simbolo_inicial is None: # si la primera produccion no ha sido agregada
            self.simbolo_inicial = var_prod # primera produccion es inicial
        self.no_terminales.add(var_prod)
        for prods in lista_producciones:
            self.producciones[var_prod].append(prods)
            for simbolo in prods:
                if not simbolo.isupper() and simbolo != EPSILON:
                    self.terminales.add(simbolo) # agrego los terminales de la gramatica

    # funcion primero

    #funcion segundo

g = Gramatica()
g.agregar_produccion('E', [['E', '+', 'T'], ['T']])
g.agregar_produccion('T', [['T', '*', 'F'], ['F']])
g.agregar_produccion('F', [['(', 'E', ')'], ['id']])

print(g.no_terminales)
print(g.terminales)