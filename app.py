import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizzaria','ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana','ativo':False}]

def exibir_nome():
    print('Sabor Express')

def exibir_opcoes(): 
    print('1- Cadastrar Restaurante')
    print('2- Listar Restaurante')
    print('3- Ativar\Desativar Restaurante')
    print('4- Sair\n')

def fechar_app():
    mostrar_subtitulo('Finalizando Aplicação')

def opcao_invalida():
    mostrar_subtitulo('Opção inválida.')
    voltar_main()

def cadastrar_restaurante():
    mostrar_subtitulo('Cadastro de Restaurantes.')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO Restaurante {nome_restaurante} foi adicionado.\n')
    voltar_main()

def mostrar_restaurantes():
    mostrar_subtitulo('Lista de Restaurantes.')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for x in restaurantes:
        #if x['ativo'] == True:
            nome_restaurante = x['nome']
            categoria = x['categoria']
            ativo = 'Ativado' if x['ativo'] else 'Desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_main()

def alternar_estado():
    mostrar_subtitulo('Ativar\Desativar Restaurante.')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_main()

def voltar_main():
    input('\nDigite uma tecla para voltar.')
    main()

def mostrar_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * len(subtitulo)
    print(linha)
    print(f'{subtitulo}')
    print(f'{linha}\n')

def escolher_opcao():
    try:
        opcao = int(input('Escolha um opção: '))

        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            mostrar_restaurantes()
        elif opcao == 3:
            alternar_estado()
        elif opcao == 4:
            fechar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()