import random
import seaborn as sns
import matplotlib.pyplot as plt

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 100) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso
    
    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres) * 100


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        if lista_pesos:
            self.peso = random.choice(lista_pesos)
            self.academia.pegar_haltere(self.peso)
        else:
            self.peso = 0

    def finalizar_treino(self):
        if self.peso == 0:
            return
        
        espacos = self.academia.listar_espacos()

        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
        elif self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)
        self.peso = 0

academia = Academia()
usuarios = [Usuario(1, academia) for _ in range(20)]
usuarios += [Usuario(2, academia) for _ in range(1)]
random.shuffle(usuarios)

list_caos = []

for _ in range(100):
    for _ in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_caos.append(academia.calcular_caos())

sns.histplot(list_caos, kde=True, bins=20)
plt.xlabel('Índice de caos (%)')
plt.ylabel('Frequência')
plt.title('Distribuição do Índice de Caos na Academia')
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))

plt.show()
