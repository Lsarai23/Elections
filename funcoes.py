# Projeto: Simulador de Urna Eletrônica
#
# Autor: Lucas P.C. Sarai
# RA: 32336888

# Arquivo com as funções usadas
#_______________________________________________________________________________________________________________________

#Criação de listas globais para armazenar os candidatos.
nomes_pref = []
nomes_gov = []
nomes_pres = []

#Criação de listas globais com os números de cada candidato.
nums_pref = []
nums_gov = []
nums_pres = []

#Criação de listas globais com os partidos dos candidatos cadastrados e votados.
partidos_pref = []
partidos_pref_votados = []
partidos_gov = []
partidos_gov_votados = []
partidos_pres = []
partidos_pres_votados = []

#Criação de listas globais com informaçõs dos eleitores: nome e CPF.
nomes_eleit = []
cpfs_eleit = []

#Criação de listas e dicionários globais para os candidatos votados.
candidatos_pref_votados = []
dic_votados_pref_partido = {}

candidatos_gov_votados = []
dic_votados_gov_partido = {}

candidatos_pres_votados = []
dic_votados_pres_partido = {}

#Lista global que armazenará os eleitores que votaram.
votantes = []

#Variáveis globais de contagem dos votos totais em cada categoria.
total_votos_pref = 0
total_votos_gov = 0
total_votos_pres = 0

#Variáveis globais de contagem dos votos válidos(não brancos e não nulos) em cada categoria.
validos_pref = 0
validos_gov = 0
validos_pres = 0

##Variáveis globais de contagem dos votos brancos em cada categoria.
brancos_pref = 0
brancos_gov = 0
brancos_pres = 0

#Variáveis globais de contagem dos votos nulos em cada categoria.
nulos_pref = 0
nulos_gov = 0
nulos_pres = 0

#Lista global para o partidos que tiveram políticos eleitos.
partidos_eleitos=[]

def tela_inicial(): #Gera a tela inicial com o menu de opções.
    print("+" * 7, "MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO", "+" * 7)
    print()
    print(" " * 15, "1.Cadastrar Candidatos")
    print(" " * 15, "2.Cadastrar Eleitores")
    print(" " * 15, "3.Votar")
    print(" " * 15, "4.Apurar Resultados")
    print(" " * 15, "5.Relatório e Estatísticas")
    print(" " * 15, "6.Encerrar")


def encerrar(): # Gera a tela de encerramento.
    print()
    print("+" * 50)
    print()
    print(" " * 7, "O GOVERNO AGRADECE A SUA PARTICIPAÇÃO.", " " * 7)
    print()
    print("+" * 50)


def cadastro_candidatos():
    print("+" * 7, "CADASTRAR CANDIDATOS:", "+" * 7)
    print()
    cadastrar_c = ''  # String vazia de confirmação do cadastro.
    while cadastrar_c.lower() != 'não': # Enquanto a resposta for "não" (minúscula ou maiúscula).
        print(" " * 13, end="")
        cargo_c = input("Cargo que disputa:") #Analisa qual categoria será preeenchida.

        if cargo_c.lower() == 'prefeito':
            print(" " * 13, end="")
            nome_pref = input("Nome:")

            print(" " * 13, end="")
            num_pref = int(input("Número:"))

            print(" " * 13, end="")
            partid_pref = input("Partido:")

            #Salva o nome, número e partido do candidato a prefeito em listas.
            nomes_pref.append(nome_pref)
            nums_pref.append(num_pref)
            partidos_pref.append(partid_pref)

        elif cargo_c.lower() == 'governador':
            print(" " * 13, end="")
            nome_gov = input("Nome:")

            print(" " * 13, end="")
            num_gov = int(input("Número:"))

            print(" " * 13, end="")
            partid_gov = input("Partido:")

            # Salva o nome, número e partido do candidato a governador em listas.
            nomes_gov.append(nome_gov)
            nums_gov.append(num_gov)
            partidos_gov.append(partid_gov)

        elif cargo_c.lower() == 'presidente':
            print(" " * 13, end="")
            nome_pres = input("Nome:")

            print(" " * 13, end="")
            num_pres = int(input("Número:"))

            print(" " * 13, end="")
            partid_pres = input("Partido:")

            # Salva o nome, número e partido do candidato a presidente em listas.
            nomes_pres.append(nome_pres)
            nums_pres.append(num_pres)
            partidos_pres.append(partid_pres)

        print(" " * 12, "Cadastrado.")
        print()
        print(" " * 13, end="")
        cadastrar_c = input("Deseja continuar (Sim ou Não): ")
        print()


def cadastrar_eleitores():
    print("+" * 7, "CADASTRAR ELEITORES:", "+" * 7)
    print()
    cadastrar_e = ''

    while cadastrar_e.lower() != 'não':
        print(" " * 13, end="")
        nome_e = input("Nome:")

        print(" " * 13, end="")
        cpf_e = input("CPF:")

        print(" " * 12, "Cadastrado.")

        #Salva o nome e CPF do eleitor em listas.
        nomes_eleit.append(nome_e)
        cpfs_eleit.append(cpf_e)

        print()
        print(" " * 13, end="")
        cadastrar_e = input("Deseja continuar (Sim ou Não): ")
        print()


def votacao():
    print("+" * 7, "VOTAÇÃO:", "+" * 7)

    #Traz para esse escopo algumas variáveis globais.
    global total_votos_pref
    global total_votos_gov
    global total_votos_pres

    global validos_pref
    global validos_gov
    global validos_pres

    global brancos_pref
    global brancos_gov
    global brancos_pres

    global nulos_pref
    global nulos_gov
    global nulos_pres

    global votantes

    print()
    print(" " * 13, end="")
    eleitor=input("Infome o CPF: ") # Insere o CPF do eleitor, para saber qual que está votando.
    votantes.append(nomes_eleit[cpfs_eleit.index(eleitor)]) #Adiciona o nome do eleitor votante em uma lista.
    print()
    print(" " * 13, "PREFEITO")
    print()
    print(" " * 13, end="")
    votacao_pref = int(input("Número: ")) # Insere o número do candidato.
    while votacao_pref == -1 or votacao_pref == -2: # Analisa se o eleitor deseja votar branco (-1) ou nulo (-2).
        if votacao_pref == -1: # Caso branco.
            print()
            print(" " * 13, end="")
            branco = input("Deseja votar Branco(Sim ou Não):") # Mensagem de confirmação.
            if branco.lower() == "não": # Caso "não".
                print()
                print(" " * 13, end="")
                votacao_pref = int(input("Número: ")) # Continua repetindo a mensagem.
            else: # Caso "sim".

                votacao_pref = 0 # Considera o número do candidato como 0.
                brancos_pref += 1 #Contabiliza no total de votos brancos em prefeitos.
                total_votos_pref += 1 #Contabiliza no total de votos totais de prefeitos.

        elif votacao_pref == -2: # Caso nulo.
            print()
            print(" " * 13, end="")
            nulo = input("Deseja votar Nulo(Sim ou Não):") # Mensagem de confirmação.
            if nulo.lower() == "não": # Caso "não".
                print()
                print(" " * 13, end="")
                votacao_pref = int(input("Número: ")) # Repete a mensagem.
            else:
                votacao_pref = 0 # Considera o número do candidato como 0.
                nulos_pref += 1 #Contabiliza no total de votos nulos de prefeitos.
                total_votos_pref += 1 #Contabiliza no total de votos totais de prefeitos.

    confirmacao = 'não'

    #Caso o eleitor escolha o número de um candidato.
    while confirmacao.lower() == 'não' and votacao_pref > 0:
        print()
        print(" " * 13, "Candidato:", nomes_pref[nums_pref.index(votacao_pref)]) # Mostra o candidato escolhido.
        print(" " * 13, "Partido:", partidos_pref[nums_pref.index(votacao_pref)]) # Mostra o partido do candidato escolhido.
        print()

    #Analisa se o eleitor deseja votar realmente no candidato selecionado. Caso não, repete o processo.
        confirmacao = input("Confirme o voto(Sim ou Não):")
        if confirmacao == 'não':
            print(" " * 13, end="")
            votacao_pref = int(input("Número: "))

    #Caso sim:
    if votacao_pref > 0:
        total_votos_pref += 1 # Contabiliza os votos para prefeito.
        validos_pref += 1 # Contabiliza os votos válidos para prefeito.
        candidatos_pref_votados.append(nomes_pref[nums_pref.index(votacao_pref)]) #Armazena o candidato selecionado.
        partidos_pref_votados.append(partidos_pref[nums_pref.index(votacao_pref)])#Armazena o partido desse candaidato.

        #Salva o candidato e partido em um dicionário, onde a chave é o candidato, e o valor é o partido.
        dic_votados_pref_partido[nomes_pref[nums_pref.index(votacao_pref)]] = partidos_pref[nums_pref.index(votacao_pref)]

    # Mesmo processo que o apresentado na categoria "Prefeito", apenas mudando as listas e dicionários.
    print(" " * 13, "GOVERNADOR")
    print()
    print(" " * 13, end="")
    votacao_gov = int(input("Número: "))
    while votacao_gov == -1 or votacao_gov == -2:
        if votacao_gov == -1:
            print()
            print(" " * 13, end="")
            branco = input("Deseja votar Branco(Sim ou Não):")
            if branco.lower() == "não":
                print()
                print(" " * 13, end="")
                votacao_gov = int(input("Número: "))
            else:
                votacao_gov = 0
                brancos_gov += 1
                total_votos_gov += 1

        elif votacao_gov == -2:
            print()
            print(" " * 13, end="")
            nulo = input("Deseja votar Nulo(Sim ou Não):")
            if nulo.lower() == "não":
                print()
                print(" " * 13, end="")
                votacao_gov = int(input("Número: "))
            else:
                votacao_gov = 0
                nulos_gov += 1
                total_votos_gov += 1

    confirmacao = 'não'
    while confirmacao.lower() == 'não' and votacao_gov > 0:
        print()
        print(" " * 13, "Candidato:", nomes_gov[nums_gov.index(votacao_gov)])
        print(" " * 13, "Partido:", partidos_gov[nums_gov.index(votacao_gov)])
        print()
        confirmacao = input("Confirme o voto(Sim ou Não):")
        if confirmacao == 'não':
            print(" " * 13, end="")
            votacao_gov = int(input("Número: "))
    if votacao_gov > 0:
        total_votos_gov += 1
        validos_gov += 1
        candidatos_gov_votados.append(nomes_gov[nums_gov.index(votacao_gov)])
        partidos_gov_votados.append(partidos_gov[nums_gov.index(votacao_gov)])
        dic_votados_gov_partido[nomes_gov[nums_gov.index(votacao_gov)]] = partidos_gov[nums_gov.index(votacao_gov)]

    # Mesmo processo que o apresentado na categoria "Prefeito", apenas mudando as listas e dicionários.
    print(" " * 13, "PRESIDENTE")
    print()
    print(" " * 13, end="")
    votacao_pres = int(input("Número: "))
    while votacao_pres == -1 or votacao_pres == -2:
        if votacao_pres == -1:
            print()
            print(" " * 13, end="")
            branco = input("Deseja votar Branco(Sim ou Não):")
            if branco.lower() == "não":
                print()
                print(" " * 13, end="")
                votacao_pres = int(input("Número: "))
            else:
                votacao_pres = 0
                brancos_pres += 1
                total_votos_pres += 1

        elif votacao_pres == -2:
            print()
            print(" " * 13, end="")
            nulo = input("Deseja votar Nulo(Sim ou Não):")
            if nulo.lower() == "não":
                print()
                print(" " * 13, end="")
                votacao_pres = int(input("Número: "))
            else:
                votacao_pres = 0
                nulos_pres += 1
                total_votos_pres += 1

    confirmacao = 'não'
    while confirmacao.lower() == 'não' and votacao_pres > 0:
        print()
        print(" " * 13, "Candidato:", nomes_pres[nums_pres.index(votacao_pres)])
        print(" " * 13, "Partido:", partidos_pres[nums_pres.index(votacao_pres)])
        print()
        confirmacao = input("Confirme o voto(Sim ou Não):")
        if confirmacao == 'não':
            print(" " * 13, end="")
            votacao_pres = int(input("Número: "))
    if votacao_pres > 0:
        total_votos_pres += 1
        validos_pres += 1
        candidatos_pres_votados.append(nomes_pres[nums_pres.index(votacao_pres)])
        partidos_pres_votados.append(partidos_pres[nums_pres.index(votacao_pres)])
        dic_votados_pres_partido[nomes_pres[nums_pres.index(votacao_pres)]] = partidos_pres[nums_pres.index(votacao_pres)]


def resultados():
    #Traz para esses escopo as mesmas variáveis da função anterior, as quais estão agora com seu valor atualizado.
    global total_votos_pref
    global total_votos_gov
    global total_votos_pres

    global validos_pref
    global validos_gov
    global validos_pres

    global brancos_pref
    global brancos_gov
    global brancos_pres

    global nulos_pref
    global nulos_gov
    global nulos_pres


    print("+" * 7, "RESULTADOS:", "+" * 7)
    print()
    dic_pref_votos = {} #Dicionário para armazenar candidadato e quantidade de votos.
    for c_pref in candidatos_pref_votados:
        dic_pref_votos[c_pref] = candidatos_pref_votados.count(c_pref) # Armazena nome como chave e votos como valor.

    #Cria um novo dicionário com as mesmas chaves e valores do dicionário acima, só que ordenadas do maior valor para o menor.
    dic_ranking_pref = {k: v for k, v in
                    sorted(dic_pref_votos.items(), key=lambda item: item[1], reverse=True)}

    #Até a linha 393, repete o processo feito na categoria Prefeito, só que para as outras categorias.

    dic_gov_votos = {}
    for c_gov in candidatos_gov_votados:
        dic_gov_votos[c_gov] = candidatos_gov_votados.count(c_gov)
    dic_ranking_gov = {k: v for k, v in
                   sorted(dic_gov_votos.items(), key=lambda item: item[1], reverse=True)}

    dic_gov_votos = {}
    for c_pres in candidatos_pres_votados:
        dic_gov_votos[c_pres] = candidatos_pres_votados.count(c_pres)
    dic_ranking_pres = {k: v for k, v in
                    sorted(dic_gov_votos.items(), key=lambda item: item[1], reverse=True)}

    #Criação das tabelas de resultados para cada categoria.

    #Observação: Apenas são exibidos os candidatos que receberam, ao mínimo, 1 voto.

    #Categoria Presidente.
    print("_" * 64)
    print("| {:^60} |".format("RANKING DO RESULTADO PARA PRESIDENTE")) #Título da tabela.
    print("_" * 64)
    print("| {:^11} | {:^11} | {:^11} | {:^11} |".format("Nome", "Partido", "Total de votos", "% votos válidos"))#Colunas.
    print("_" * 64)
    i = 1



    #Preenche as linhas de acordo com as colunas correspondentes, seguindo a ordem decrescente de votos.
    for c_pres_ordem in dic_ranking_pres:
        print("| {}.{:^9} | {:^11} | {:^14} | {:^15.1f} |".format(i, c_pres_ordem, dic_votados_pres_partido[c_pres_ordem],
                                                                  dic_ranking_pres[c_pres_ordem],
                                                                  (dic_ranking_pres[c_pres_ordem] / validos_pres) * 100))
        #Salva o partido que teve seu candidato eleito.
        if i == 1:
            partidos_eleitos.append(dic_votados_pres_partido[c_pres_ordem])
        i += 1
        print("_" * 64)

    #Linhas com informaçãoes gerais

    print("| {}: {}{:^44}|".format("Total de votos", total_votos_pres," "))
    print("| {}: {} ({}%){:^25}|".format("Total de votos válidos e %", validos_pres,
                                       str(int((validos_pres / total_votos_pres) * 100)).zfill(3)," "))
    print("| {}: {} ({}%){:^31}|".format("Total de brancos e %", brancos_pres,
                                         str(int((brancos_pres / total_votos_pres) * 100)).zfill(3)," "))
    print("| {}: {} ({}%){:^33}|".format("Total de nulos e %", nulos_pres,
                                         str(int((nulos_pres / total_votos_pres) * 100)).zfill(3)," "))
    print("_" * 64)

    print()

    #Mesma lógica da tabela anterior, só que adaptada a categoria Governador.
    print("_" * 64)
    print("| {:^60} |".format("RANKING DO RESULTADO PARA GOVERNADOR"))
    print("_" * 64)
    print("| {:^11} | {:^11} | {:^11} | {:^11} |".format("Nome", "Partido", "Total de votos", "% votos válidos"))
    print("_" * 64)
    i = 1
    for c_gov_ordem in dic_ranking_gov:
        print("| {}.{:^9} | {:^11} | {:^14} | {:^15.1f} |".format(i, c_gov_ordem, dic_votados_gov_partido[c_gov_ordem],
                                                                  dic_ranking_gov[c_gov_ordem],
                                                                  (dic_ranking_gov[c_gov_ordem] / validos_gov) * 100))
        # Salva o partido que teve seu candidato eleito.
        if i == 1:
            partidos_eleitos.append(dic_votados_gov_partido[c_gov_ordem])
        i += 1
        print("_" * 64)

    print("| {}: {}{:^44}|".format("Total de votos", total_votos_gov," "))
    print("| {}: {} ({}%){:^25}|".format("Total de votos válidos e %", validos_gov,
                                       str(int((validos_gov / total_votos_gov) * 100)).zfill(3)," "))
    print("| {}: {} ({}%){:^31}|".format("Total de brancos e %", brancos_gov,
                                         str(int((brancos_gov / total_votos_gov) * 100)).zfill(3)," "))
    print("| {}: {} ({}%){:^33}|".format("Total de nulos e %", nulos_gov,
                                         str(int((nulos_gov / total_votos_gov) * 100)).zfill(3)," "))
    print("_" * 64)

    print()

    # Mesma lógica da tabela anterior, só que adaptada a categoria Prefeito.
    print("_" * 64)
    print("| {:^60} |".format("RANKING DO RESULTADO PARA PREFEITO"))
    print("_" * 64)
    print("| {:^11} | {:^11} | {:^11} | {:^11} |".format("Nome", "Partido", "Total de votos", "% votos válidos"))
    print("_" * 64)
    i = 1
    for c_pref_ordem in dic_ranking_pref:
        print("| {}.{:^9} | {:^11} | {:^14} | {:^15.1f} |".format(i, c_pref_ordem, dic_votados_pref_partido[c_pref_ordem],
                                                                  dic_ranking_pref[c_pref_ordem],
                                                                  (dic_ranking_pref[c_pref_ordem] / validos_pref) * 100))
        # Salva o partido que teve seu candidato eleito.
        if i == 1:
            partidos_eleitos.append(dic_votados_pref_partido[c_pref_ordem])
        i += 1
        print("_" * 64)

    print("| {}: {}{:^44}|".format("Total de votos", total_votos_pref," "))
    print("| {}: {} ({}%){:^25}|".format("Total de votos válidos e %",
                                            validos_pref,str(int((validos_pref / total_votos_pref) * 100)).zfill(3)," "))
    print("| {}: {} ({}%){:^31}|".format("Total de brancos e %",
                                            brancos_pref, str(int((brancos_pref / total_votos_pref) * 100)).zfill(3)," "))
    print("| {}: {} ({}%){:^33}|".format("Total de nulos e %", nulos_pref, str(int((nulos_pref / total_votos_pref) * 100)).zfill(3)," "))
    print("_" * 64)
def relatorio_estatisticas():
    print("+" * 7, "RELATÓRIO E ESTATÍSTICAS:", "+" * 7)
    print()
    print("Votantes:")
    print()
    votantes.sort() # Ordena os eleitores votantes em ordem alfabética.
    for eleit_v in votantes: # Exibe esses votantes.
        print("-> {}".format(eleit_v))
    print()

    # Exibe e analisa se a quantidade de eleitores cadastrados e votantes é similar.
    print("Quantidade de eleitores votantes /eleitores cadastrados: {}/{}".format(len(votantes), len(nomes_eleit)))
    if len(votantes) == len(nomes_eleit): # Caso sejam equivalentes.
        print("Todos os cadastrdos votaram.")
        print()

    #Ordenamento de forma decrescente da quantidade de políticos eleitos por partido.
    aux={}
    for p in partidos_eleitos[:3]:
        aux[p]=partidos_eleitos[:3].count(p)
    ordem_p_eleitos = {k: v for k, v in
                    sorted(aux.items(), key=lambda item: item[1], reverse=True)}
    partidos_e=list(ordem_p_eleitos.keys()) # Partidos com políticos eleitos.
    votos_partidos=list(ordem_p_eleitos.values()) # Quantidade de políticos eleitos por partido.

    # Mostra o partido que mais e o que menos elegeu políticos, com as respectivas quantidades de políticos eleitos.
    print("Partido que elegeu mais políticos:{} ({})".format(partidos_e[0],votos_partidos[0]))
    print("Partido que menos elegeu políticos:{} ({})".format(partidos_e[len(partidos_e) - 1],votos_partidos[len(votos_partidos) - 1]))
