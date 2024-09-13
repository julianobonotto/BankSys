class Cliente():
    def __init__(self, pessoa_fisica):
        self.pessoa_fisica = pessoa_fisica
        self.contas = []
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def realizar_trasacao():
        pass

    def adicionar_conta():
        pass
    

