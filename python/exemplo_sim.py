import salabim as sim
'''
class Modelo(sim.Component):
    def process(self):
        ano = 2000
        while True:
            print(f"Ano: {ano}")
            ano += 1
            self.hold(1)  # Avança o tempo em 1 unidade (representando 1 ano)

# Cria o ambiente de simulação
env = sim.Environment()
# Instancia o processo Ano
ano = Modelo()
# Executa a simulação até o ano 2020
env.run(till=21)  # 21 unidades de tempo, de 2000 a 2020 inclusivo
'''

import salabim as sim
import random

import salabim as sim
'''
class Produtor(sim.Component):
    def process(self):
        for i in range(1, 6):  # Produz 5 valores, por exemplo
            print(f"Produtor produzindo valor: {i}")
            lista_entre_componentes.append(i)  # Adiciona o valor à lista
            consumidor.activate()  # Ativa o Consumidor caso esteja passivado
            self.hold(1)  # Espera 1 unidade de tempo antes de produzir o próximo valor

class Consumidor(sim.Component):
    def process(self):
        while True:
            if lista_entre_componentes:  # Verifica se há itens na lista
                valor = lista_entre_componentes.pop(0)  # Retira o primeiro valor da lista
                print(f"Consumidor consumindo valor: {valor}")
                self.hold(2)  # Tempo para processar o valor
            else:
                self.passivate()  # Aguarda até que o Produtor produza mais valores



class Produtor(sim.Component):
    def process(self):
        i = 0
        while True:
            i = i + 1
        #for i in range(1, 6):  # Produz 5 valores, por exemplo
            print(f"[Tempo {env.now()}] Produtor produzindo valor: {i}")
            lista_entre_componentes.append(i)  # Adiciona o valor à lista
            consumidor.activate()  # Ativa o Consumidor caso esteja passivado
            self.hold(1)  # Espera 1 unidade de tempo antes de produzir o próximo valor

class Consumidor(sim.Component):
    def process(self):
        while True:
            if lista_entre_componentes:  # Verifica se há itens na lista
                valor = lista_entre_componentes.pop(0)  # Retira o primeiro valor da lista
                print(f"[Tempo {env.now()}] Consumidor consumindo valor: {valor}")
                self.hold(1)  # Tempo para processar o valor
            else:
                self.passivate()  # Aguarda até que o Produtor produza mais valores


# Cria o ambiente de simulação
env = sim.Environment()

# Cria a lista compartilhada entre os componentes
lista_entre_componentes = []

# Instancia os componentes Produtor e Consumidor
produtor = Produtor()
consumidor = Consumidor()

# Executa a simulação por tempo suficiente para que todos os valores sejam consumidos
env.run(till=10)
'''
