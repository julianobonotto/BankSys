import decimal as d
from datetime import datetime

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaCorrente:
     def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.operacoes_financeiras = []

class Cliente():
     def __init__(self, pessoa_fisica):
        self.pessoa_fisica = pessoa_fisica
        self.contas = []
        self.indice_conta = 0

class Saque_ou_deposito():
    def __init__(self, operacao, valor):
        self.data_hora = datetime.now()
        self.operacao = operacao
        self.valor = valor


def valida_decimal():
    input_retorno = 0
    input_cliente = input("Digite valor da operacao: ")
    try:
        input_cliente = d.Decimal(input_cliente)
        if input_cliente > 0.0:
            input_retorno = input_cliente
        else:
            print("Numero menor que zero - OPERAÇÃO INVALIDA")
    except Exception as err:
        print("valor digitado inválido")
        pass
    return input_retorno

def realiza_operacao_financeira(extrato, valor, operacao):
    data_hora = datetime.now()
    extrato += f"{data_hora}  {operacao}  R${valor:.2f}\n"
    return extrato

def adiciona_linha_extrato(extrato, valor, operacao):
    data_hora = datetime.now()
    extrato += f"{data_hora}  {operacao}  R${valor:.2f}\n"
    return extrato

def busca_cpf_cadastrado(cpf, clientes_cadastrados):
    return [cliente for cliente in clientes_cadastrados if cliente.cpf == cpf]

def cadastra_cliente(clientes_cadastrados):
    cpf = input("Digite CPF: ")
    nome = input("Digite Nome: ")
    data_nascimento = input("Data Nascimento: ")
    endereco = input("Endereço: ")

    cliente_filtrado = busca_cpf_cadastrado(cpf, clientes_cadastrados)
    if cliente_filtrado:
            print("CPF/cliente já cadastrado")
    else:
        clientes_cadastrados.append(PessoaFisica(cpf = cpf, nome = nome, data_nascimento = data_nascimento, endereco = endereco))

    return clientes_cadastrados

def lista_clientes(clientes_cadastrados):
    for cli in clientes_cadastrados:
        print(cli.cpf, " ", cli.nome, " ", cli.data_nascimento, " ", cli.endereco)

def cadastra_nova_conta(clientes_cadastrados, proximo_numero_de_conta):
    nova_conta = 0
    cpf = input("Digite CPF do Cliente: ")
    cliente_cadastrado = busca_cpf_cadastrado(cpf, clientes_cadastrados)
    if cliente_cadastrado:
        nova_conta = ContaCorrente(proximo_numero_de_conta, cliente_cadastrado)
        proximo_numero_de_conta = gera_numero_conta_nova(proximo_numero_de_conta)
    else:
        print("CPF não cadastrado, impossivel abrir conta")

    return nova_conta, proximo_numero_de_conta

def gera_numero_conta_nova(proximo_numero_de_conta):
    proximo_numero_de_conta += 1
    return proximo_numero_de_conta


def sys_bank():
    saldo = 0
    contador_saque = 0
    extrato = '===========EXTRATO============\n'
    LIMITE_NUMERO_SAQUE_DIARIO = 3
    LIMITE_VALOR_SAQUE_POR_OPERACAO = 500.00
    clientes_cadastrados = []
    contas = []
    proximo_numero_de_conta = 1000

    menu = """
[nc] Novo Cliente
[lc] Lista Cliente
[cc] Nova Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    while True:
        opcao = input(menu)
        if opcao == "d":
            print("Depositar")
            conta_para_deposito = input("Informe a Conta Corrente: ")
            #buscar dentro de -> contas
            for conta in contas:
                if str(conta.numero) == conta_para_deposito:
                    valor = 0
                    valor += valida_decimal()
                    if valor > 0 :
                        deposito = Saque_ou_deposito("DEPOSITO", valor)
                        conta.operacoes_financeiras.append(deposito)
                        conta.saldo += valor
                else:
                    print("conta não cadastrada")            

        elif opcao == "s":
            print("Sacar")
            conta_para_saque = input("Informe a Conta Corrente: ")
            #buscar dentro de -> contas
            for conta in contas:
                if str(conta.numero) == conta_para_saque:
                    valor = 0
                    valor += valida_decimal()
                    if (valor > 0 
                        and conta.saldo >= valor 
                        and contador_saque < LIMITE_NUMERO_SAQUE_DIARIO 
                        and valor <= LIMITE_VALOR_SAQUE_POR_OPERACAO):
                        saque = Saque_ou_deposito("SAQUE  -", valor)
                        conta.operacoes_financeiras.append(saque)
                        conta.saldo -= valor
                else:
                    print("conta não cadastrada")        

        elif opcao == "nc":
            print("Cadastro de Cliente")
            clientes_cadastrados = cadastra_cliente(clientes_cadastrados)
            for cli in clientes_cadastrados:
                print(cli.nome)

        elif opcao == "lc":
            print("Lista de Clientes")
            lista_clientes(clientes_cadastrados)

        elif opcao == "cc":
            print("Cadastra Nova Conta")
            nova_conta, proximo_numero_de_conta = cadastra_nova_conta(clientes_cadastrados, proximo_numero_de_conta)
            if nova_conta == 0:
                print("Nao cadastrado")
            else:
                contas.append(nova_conta)
                print("Nome Cliente = ", nova_conta.cliente[0].nome, " Numero Conta = ", nova_conta.numero," Saldo = ", nova_conta.saldo)
        
        elif opcao == "e":
            conta_corrente_informada = input("Digite numero conta para ver extrato: ")
            for conta in contas:
                if str(conta.numero) == conta_corrente_informada:
                    print(f"Extrato da conta de Numero = {conta.numero}\n")   
                    for operacao_financeira in conta.operacoes_financeiras:
                        print(operacao_financeira.data_hora, "   ", operacao_financeira.operacao, "   ", operacao_financeira.valor)
                    print("\n==========================\n SALDO EM CONTA = ", conta.saldo)

        elif opcao == "q":
            print("Sair")
            break
        else:
            print("Opção inválida")



if __name__ == '__main__':
    print('Iniciando Sys Bank')
    sys_bank()