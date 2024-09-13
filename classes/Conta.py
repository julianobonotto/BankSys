
class Conta:
     def __init__(self, cliente_pf, proximo_numero_de_conta):
        self.agencia = "0001"
        self.numero = proximo_numero_de_conta
        self.cliente_pf = cliente_pf
        self.saldo = 0
        self.historico_transacoes = []


     def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

     def adiciona_transacao(self, transacao):
         self.historico_transacoes.append(transacao)

     def atualiza_saldo(self, deposito):
          self.saldo += deposito

     def extrato(self):
         for transacao in self.historico_transacoes:
             print(transacao)

