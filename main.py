from locadoraV4 import *
from operacoesbd import *

opcao = 6

conexao = abrirBancoDados('localhost', 'root', '12345', 'locadorav4')

while opcao != 5:
    opcao = menu()

    if opcao == 1:
        listarFilmes(conexao)

    elif opcao == 2:
        inserirNovoFilme(conexao)

    elif opcao == 3:
        listarFilmes(conexao)
        pesquisarPeloCodigo(conexao)

    elif opcao == 4:
        listarFilmes(conexao)
        excluirPeloCodigo(conexao)

encerrarBancoDados(conexao)

print('Obrigado por utilizar a locadora V4, volte sempre!')



