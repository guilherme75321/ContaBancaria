def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite,
        "tipo_de_conta": "corrente"  # Adicionei "tipo_de_conta" como chave no dicionário
    }
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, tipo_de_conta, valor):
    if tipo_de_conta == "corrente":
        conta["saldo"] -= valor
    elif tipo_de_conta == "poupanca":
        # Adicione lógica para sacar da poupança, se necessário
        pass
    else:
        print("Tipo de conta inválido")

def extrato(conta):
    print(f"Número da conta: {conta['numero']}")
    print(f"Saldo atual: {conta['saldo']}")
