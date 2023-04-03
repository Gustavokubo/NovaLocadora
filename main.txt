from locadora import *
from operacoesbd import *

opcao = 6

conexao = abrirBancoDados('localhost', 'root', '12345', 'novalocadora')

while opcao != 5:

    opcao = menu()

    if opcao == 1:
        listarFilmes(conexao)

    elif opcao == 2:
        inserirFilmes(conexao)

    elif opcao == 3:
        listarFilmes(conexao)
        pesquisarCodigo(conexao)

    elif opcao == 4:
        listarFilmes(conexao)
        excluirPeloCodigo(conexao)

encerrarBancoDados(conexao)

print('Obrigado por utilizar a locadora V3, volte sempre!')