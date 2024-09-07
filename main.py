import decimal as d
import datetime as dt

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

def adiciona_linha_extrato(extrato, valor, operacao):
    data_hora = dt.datetime.now()
    extrato += f"{data_hora}  {operacao}  R${valor:.2f}\n"
    return extrato


def sys_bank():
    saldo = 0
    contador_saque = 0
    extrato = '===========EXTRATO============\n'
    LIMITE_NUMERO_SAQUE_DIARIO = 3
    LIMITE_VALOR_SAQUE_POR_OPERACAO = 500.00

    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    while True:
        opcao = input(menu)
        if opcao == "d":
            deposito = 0
            print("Depositar")            
            deposito += valida_decimal()
            if deposito > 0 :
                saldo += deposito
                extrato = adiciona_linha_extrato(extrato, deposito, " -> DEPOSITO.... +")
            print(f"o slado é = {saldo}")

        elif opcao == "s":
            print("Sacar")
            saque = 0
            saque += valida_decimal()
            if (saque > 0 
                and saldo >= saque 
                and contador_saque < LIMITE_NUMERO_SAQUE_DIARIO 
                and saque <= LIMITE_VALOR_SAQUE_POR_OPERACAO):
                saldo -= saque
                contador_saque += 1
                extrato = adiciona_linha_extrato(extrato, saque, " -> SAQUE....... -")
            else:
                print("Condiçoes para saque não atendidas")
            print(f"o slado é = {saldo}")


        elif opcao == "e":
            print_extrato = ""
            print_extrato += f"{extrato}\n==============================\n Saldo atual  =  R$  {saldo:.2f}\n"
            print(print_extrato)
        elif opcao == "q":
            print("Sair")
            break
        else:
            print("Opção inválida")



if __name__ == '__main__':
    print('Iniciando Sys Bank')
    sys_bank()



