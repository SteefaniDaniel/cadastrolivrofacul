

#cadastro de livros
def cadastrar_livro(id):
    nome = input('Digite o nome do livro:').upper()
    autor = input('Digite o autor do livro:')
    editora = input('Digite a editora do livro:')

    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}

    lista_livro.append(livro)


#consulta de livros
def consultar_livro():
    while True:
        opcao= int(input('Escolha uma opção:\n1.Consultar Todos\n2.Consultar por id\n3.Consultar Autor\n4.Retornar ao menu'))

        if opcao == '1':
            for livro in lista_livro:
                print(livro)
        elif opcao == '2':
            id.consultar = int(input('Digite o id do livro que quer consultar:'))
            for livro in lista_livro:
                if livro['id'] == id.consultar:
                    print(livro)
                    break
            else:
                print('Este livro não foi encontrado.')
        elif opcao == '3':
            id.autor = input('Digite o autor do livro que deseja consultar:')
            for livro in lista_livro:
                if livro['autor'] == id.autor:
                    print(livro)
        elif opcao == '4':
            return
        else:
            print('Opção inválida!')


def remover_livro():
    livro_remove = int(input('Digite o id do livro que deseja remover:'))
    for livro in lista_livro:
        if livro['id'] == livro_remove:
            lista_livro.remove(livro)
            print('Livro removido...')
            return
    else:
        print('Este livro não foi encontrado.')

#programa principal
print('Olá,seja bem vindo ao sistema de gerenciamento de pessoas da Stéfani!')

while True:
    id_global = 0
    menu = input('Escolha uma opção:\n1.Cadastrar livro\n2.Consultar livro\n3.Remover livro\n4.Encerrar programa\n>>')
    if menu == '1':
        cadastrar_livro(id_global)
        id_global += 1
    elif menu == '2':
        consultar_livro()
    elif menu == '3':
        remover_livro()
    elif menu == '4':
        print('Encerrando programa...')
        break
    else:
        print('Opão inválida!')

lista_livro = []
id_global = 0







