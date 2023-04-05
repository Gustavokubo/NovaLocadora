from operacoesbd import *

def menu():
    print('##################################')
    print('#    Bem vindo a locadora V4     #')
    print('#================================#')
    print('# 1) Listar filmes,              #')
    print('# 2) Inserir novo filme          #')
    print('# 3) Pesquisar filme pelo código #')
    print('# 4) Excluir filme pelo código   #')
    print('# 5) Sair                        #')
    print('##################################')
    print()
    opcao = int(input('Digite sua opção: '))
    return opcao

def listarFilmes(conexao):

    consultarListarFilmes = 'select * from filmes'
    listarFilmes = listarBancoDados(conexao, consultarListarFilmes)

    if len(listarFilmes) == 0:
            print('Não existem filmes cadastrados até o momento')
            print()
    else:
        for filme in listarFilmes:
            print('Código', filme[0],':', 'possui o titulo:', filme[1],',', 'apresentando a sinopse:', filme[2])
    print()

def inserirNovoFilme(conexao):

    titulo = input('Digite o tituli do novo filme: ')
    sinopse = input('Digite a sinopse do novo filme: ')

    consultarInserir = 'insert into filmes (titulo, sinopse) values (%s, %s)'
    dados = (titulo, sinopse)
    insertNoBancoDados(conexao, consultarInserir, dados)
    print('O filme foi adicionado com sucesso!')
    print()

def pesquisarPeloCodigo(conexao):

    codigo = input('Digite o código do filme a ser pesquisado: ')

    codigoPesquisa = 'select * from filmes where codigo =' + codigo
    listarFilmes = listarBancoDados(conexao, codigoPesquisa)

    if len(listarFilmes) == 0:
        print('código inexistente')
        print()
    else:
        for filme in listarFilmes:
            print('Código pesquisado = ',filme[0], ', filme:', filme[1], ', com sinopse:', filme[2])
    print()
def excluirPeloCodigo(conexao):

    codigo = int(input('Digite o código do filme a ser removido: '))

    consultaExclusao = 'delete from filmes where codigo = %s'
    dados = (codigo,)

    linhasExcluidas = excluirBancoDados(conexao, consultaExclusao, dados)

    if linhasExcluidas == 0:
        print('código inexistente')
        print()
    else:
        print('Filme excluido com sucesso!')
        print()
