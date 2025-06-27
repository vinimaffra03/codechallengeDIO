# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# : Aplique o desconto se o cupom for válido:

if cupom in descontos:
    novo_valor = preco - (preco * descontos[cupom])

    print('{:.2f}'.format(novo_valor))
else: 
    print('Cupom inválido')

# =================================================================================================================================================

# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

def email_valido():
    if (
        '@' in email
        and not email.startswith('@')
        and ' ' not in email
        and email.endswith(('gmail.com', 'outlook.com'))
    ):
        print('E-mail válido')
    else:
        print('E-mail inválido')
email_valido()