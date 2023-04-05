from operacoesbd import *

def menu():
    print()
    print('Bem vindo a locadora V3')
    print()
    print('1 listar, 2 inserir, 3 pesquisar pelo código, 4 excluir pelo código, 5 sair')
    print()
    opcao = int(input('Digite sua opção: '))
    return opcao

def listarFilmes(conexao):

    consultarListarFilme = 'select * from filmes'
    listarFilmes = listarBancoDados(conexao, consultarListarFilme)

    if len(listarFilmes) == 0:
        print('Não existem filmes cadastrado!')
    else:
        for filmes in listarFilmes:
            print('Código', filmes[0], ',possui o titulo: ', filmes[1], ',apresentando a sinopse:', filmes[2] )

def inserirFilmes(conexao):

    titulo = input('Digite o nome do novo filme: ')
    sinopse = input('Digite a sinopse do novo filme: ')

    consultaInserir = 'insert into filmes (titulo, sinopse) values (%s, %s)'
    dados = (titulo, sinopse)
    insertNoBancoDados(conexao, consultaInserir, dados)
    print('O filme foi adicionado com sucesso!')

def pesquisarCodigo(conexao):

    codigo = input('Digite o código do filme: ')

    consultaPesquisar = 'select * from filmes where codigo = ' + codigo
    listarFilmes = listarBancoDados(conexao, consultaPesquisar)

    if len(listarFilmes) == 0:
        print('Código não existente!')
    else:
        for item in listarFilmes:
            print(item)

def excluirPeloCodigo(conexao):

    codigo = int(input('Digite o código do filme: '))
    consultaExclusao = 'delete from filmes where codigo = %s'
    dados = (codigo,)

    linhasExcluidas = excluirBancoDados(conexao, consultaExclusao, dados)

    if linhasExcluidas == 0:
        print('Código não existente!')
    else:
        print('Filme excluido com sucesso!')
