# Projeto: Simulador de Urna Eletrônica.
#
# Autor: Lucas P.C. Sarai
# RA: 32336888

# Arquivo de execução.
# _______________________________________________________________________________________________________________________

# Traz para esse arquivo as funções utilizadas
import funcoes

# Nas linhas seguintes, solicita ao usuário uma das opções do menu e
# executa a função correspondente.
# Após cada função, sempre retorna para a tela principal.
# Caso ele selecione 6, encerra o programa.

opc = 0
while opc != 6:
    funcoes.tela_inicial()
    print(" " * 16, end="")
    opc = int(input("Opção escolhida:"))
    if opc == 1:
        funcoes.cadastro_candidatos()
    elif opc == 2:
        funcoes.cadastrar_eleitores()
    elif opc == 3:
        funcoes.votacao()
    elif opc == 4:
        funcoes.resultados()
    elif opc == 5:
        funcoes.relatorio_estatisticas()
funcoes.encerrar()
