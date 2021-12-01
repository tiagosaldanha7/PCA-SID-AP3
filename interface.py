def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
        else:
            return n

def linha(tam=42):
    return '_' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    print('                PCA - SID')
    print(linha())
    print('Integrantes do projeto SARS-TECH')
    print('''
            Amanda Luisy da Silva
            Gabriel Antonio Rodrigues Barba
            Hiago Muller Silva Henriques
            Marcelo Heugenio da Costa Moura
            Tiago Saldanha Borges
            ''')
    print(linha())
    print('            Escolha a vacina          ')
    print(linha())

def menu(lista):
    cabeçalho('Menu principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -\033[34m {item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[32mDigite sua Opção: \033[m')
    return opc
