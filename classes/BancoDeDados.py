class BancoDeDados:
     def __init__(self):
        self.pessoas_fisicas = []
        self.clientes = []
        self.contas = []
        self.numero_proxima_conta_corrente = 1000

     def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

     def lista_contas(self):
         return self.contas
     
     def adiciona_pessoa_fisica(self, pessoa_fisica):
         self.pessoas_fisicas.append(pessoa_fisica)

     def lista_pessoa_fisica(self):
         return self.pessoas_fisicas

     def fornece_numero_conta_corrente(self):
         proximo_numero_fornecido = self.numero_proxima_conta_corrente
         self.numero_proxima_conta_corrente += 1
         return proximo_numero_fornecido
     
     def adiciona_conta(self, conta_corrente):
         self.contas.append(conta_corrente)