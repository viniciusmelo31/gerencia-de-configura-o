class PortoSeco:
    def __init__(self):
        self.pilhas = [[] for _ in range(4)]  #Inicia 4 Pilhas 
    
    def empilhar_container(self, codigo):
        if self._codigo_existe(codigo):
            print("Código inválido! O container já existe.")
            return
        
        pilha = self._encontrar_pilha_menos_cheia()
        
        if len(pilha) >= 3:
            print("Impossível empilhar: Todas as pilhas estão cheias.")
            return
        
        pilha.append(codigo)
        print(f"Container {codigo} empilhado na pilha {self.pilhas.index(pilha) + 1}.")
        self._mostrar_status_pilhas()
    
    def desempilhar_container(self, codigo):
        pilha = self._encontrar_pilha_contem(codigo)
        
        if pilha is None:
            print("Código inválido! O container não existe.")
            return
        
        if pilha[-1] != codigo:
            print("Impossível desempilhar!: O container não está no topo da pilha.")
            return
        
        pilha.pop()
        print(f"Container {codigo} removido da pilha {self.pilhas.index(pilha) + 1}.")
        self._mostrar_status_pilhas()
    
    def _codigo_existe(self, codigo):
        for pilha in self.pilhas:
            if codigo in pilha:
                return True
        return False
    
    def _encontrar_pilha_menos_cheia(self):
        min_len = float('inf')
        min_pilha = None
        
        for pilha in self.pilhas:
            if len(pilha) < min_len:
                min_len = len(pilha)
                min_pilha = pilha
        
        return min_pilha
    
    def _encontrar_pilha_contem(self, codigo):
        for pilha in self.pilhas:
            if codigo in pilha:
                return pilha
        return None
    
    def _mostrar_status_pilhas(self):
        print("\nStatus das pilhas:")
        for i, pilha in enumerate(self.pilhas, start=1):
            print(f"Pilha {i}: {pilha}")

# Criar uma instância do PortoSeco
porto = PortoSeco()

# Exemplos de uso
while True:
    print("\nOpções:")
    print("1 - Empilhar container")
    print("2 - Desempilhar container")
    print("3 - Sair")
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        codigo = input("Digite o código do container: ")
        porto.empilhar_container(codigo)
    elif escolha == 2:
        codigo = input("Digite o código do container a ser removido: ")
        porto.desempilhar_container(codigo)
    elif escolha == 3:
        break
    else:
        print("Opção inválida. Escolha novamente.")
