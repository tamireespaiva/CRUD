from crud import MyCrud
crud = MyCrud('moleza.sqlite')
crud.criarTabela()

while True:
    print('''
        Escolha uma das opções abaixo:
        1 - Incluir
        2 - Ler
        3 - Alterar
        4 - Deletar
        5 - Sair
    ''')
    
    valor = input ('=>')
    if valor == '1':
        nome = input("Digite o seu nome: ")
        cpf = input("Digite o seu CPF: ")

        if len (cpf) > 11:
            print("O CPF tem mais que 11 caracteres, corrigia-o para que seja armazenado!")
        else:
            crud.inserir(nome, cpf)
    
    elif valor == '2':
        crud.selecionar()
   
    
    elif valor == '3':
        identificador = int(input("Digite o valor do identificador que deseja alterar: "))
        nome = input('Qual o novo nome: ')
        cpf = input('Qual o novo cpf: ')
    
        if len (cpf) > 11:
            print("O CPF tem mais que 11 caracteres, corrigia-o para que seja armazenado!")
        else:
            crud.alterar(identificador, nome, cpf)

    
    elif valor == '4':
        identificador = int(input("Digite o valor do identificador que deseja deletar: "))
        crud.deletar(identificador)
    
    elif valor == '5':
        break

crud.fecharDB()
