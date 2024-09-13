class ContaCorrente:
     def __init__(self, limite, limite_saque):
        self.limite = limite
        self.limite_saque = limite_saque

     def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
