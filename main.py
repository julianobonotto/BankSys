import decimal as d
from datetime import datetime
from classes.PessoaFisica import PessoaFisica
from classes.BancoDeDados import BancoDeDados
from classes.Conta import Conta

def cadastra_nova_pessoa_fisica(banco_de_dados):
    cpf = input("Digite CPF: ")
    pessoa_esta_cadastrada, pessoa = busca_cpf_pessoa_fisica_cadastrado(cpf, banco_de_dados.lista_pessoa_fisica())
    if pessoa_esta_cadastrada == False:
        nome = input("Digite Nome: ")
        data_nascimento = input("Digite Data Nascimento: ")
        nova_pessoa_fisica = PessoaFisica(cpf, nome, data_nascimento)
        banco_de_dados.adiciona_pessoa_fisica(nova_pessoa_fisica)
    else:
        print("Pessoa já cadastrada")
    return banco_de_dados

def busca_cpf_pessoa_fisica_cadastrado(cpf, pessoas_fisicas):
    for pessoa in pessoas_fisicas:
        if cpf == pessoa.cpf:
            return True, pessoa
    return False, 0

def cadastra_nova_conta_corrente(banco_de_dados):
    cpf = input("Digite CPF do Cliente: ")
    pessoa_esta_no_db, cliente_cadastrado = busca_cpf_pessoa_fisica_cadastrado(cpf, banco_de_dados.lista_pessoa_fisica())
    if pessoa_esta_no_db:
        nova_conta = Conta(cliente_cadastrado, banco_de_dados.fornece_numero_conta_corrente())
        banco_de_dados.adiciona_conta(nova_conta)
        return banco_de_dados
    else:
        print("CPF não cadastrado, impossivel abrir conta")
        return banco_de_dados
    
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

def sys_bank():
    banco_de_dados = BancoDeDados()

    menu = """
[nc] Novo Cliente / Pessoa Fisica
[lc] Lista Cliente / Pessoa Fisica
[cc] Nova Conta
[lcc] Lista Contas Corente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    while True:
        opcao = input(menu)
        if opcao == "nc":
            print("Cadastro Novo Cliente / PF")
            banco_de_dados = cadastra_nova_pessoa_fisica(banco_de_dados)

        elif opcao == "d":
            print("Depositar")
            conta_para_deposito = input("Informe a Conta Corrente: ")
            for conta in banco_de_dados.lista_contas():
                if str(conta.numero) == conta_para_deposito:
                    valor = 0
                    valor += valida_decimal()
                    if valor > 0 :
                        conta.adiciona_transacao(f"{datetime.now()}    DEPOSITO    + {valor}")
                        conta.atualiza_saldo(valor)
                else:
                    print("conta não cadastrada")    
    
        elif opcao == "s":
            print("Sacar")
            conta_para_saque = input("Informe a Conta Corrente: ")
            for conta in banco_de_dados.lista_contas():
                if str(conta.numero) == conta_para_saque:
                    valor = 0
                    valor += valida_decimal()
                    if valor > 0 :
                        conta.adiciona_transacao(f"{datetime.now()}    SAQUE       - {valor}")
                        conta.atualiza_saldo(-abs(valor))
                else:
                    print("conta não cadastrada")    

        elif opcao == "lc":
            print("Lista de Clientes / PF")
            for cliente in banco_de_dados.lista_pessoa_fisica():
                print(f"CPF = {cliente.cpf} , Nome = {cliente.nome} , Data Nasc = {cliente.data_nascimento}")

        elif opcao == "lcc":
            print("Lista Contas Correntes")
            for conta in banco_de_dados.lista_contas():
                print(f"CC = {conta.numero} , Cliente = {conta.cliente_pf} , saldo = {conta.saldo}")

        elif opcao == "cc":
            print("Cadastra Nova Conta")
            banco_de_dados  = cadastra_nova_conta_corrente(banco_de_dados)
        
        elif opcao == "e":
            print("Extrato")
            conta_corrente_informada = input("Digite numero conta para ver extrato: ")
            for conta in banco_de_dados.lista_contas():
                if str(conta.numero) == conta_corrente_informada:
                    print(f"Extrato da conta de Numero = {conta.numero}\n")
                    print(conta.extrato())
                    print("\n==========================\n SALDO EM CONTA = ", conta.saldo)

        elif opcao == "q":
            print("Sair")
            break

        else:
            print("Opção inválida")



if __name__ == '__main__':
    print('Iniciando Sys Bank')
    sys_bank()