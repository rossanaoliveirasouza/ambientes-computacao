def needleman_wunsch(seq1, seq2, igual=5, diferente=-2, lacuna=-6):
    
    # quantidade de linhas = tamaho da primeira sequencia + 1, pra colocar o valor da inicialização
    linhas = len(seq1) + 1 
    
    # quantidade de colunas = tamaho da segunda sequencia + 1, pra colocar o valor da inicialização
    colunas = len(seq2) + 1 

    # inicialização da matriz - todos valores iguais a zero
    matriz = [[0] * colunas for _ in range(linhas)] 

    # imprimi a matriz inicial - todos valores iguais a zero
    for j in matriz:
        print(j)

########################################################################################################

    # inicialização das bordas com penalidades de lacuna
    for linha in range(linhas):
        # penalidades das linhas
        matriz[linha][0] = linha * lacuna 
    
    for coluna in range(colunas):
        # penalidades das colunas
        matriz[0][coluna] = coluna * lacuna 
    
    # imprimi a matriz com os valores das penalidades
    for linha in matriz:
        print(linha)

########################################################################################################

    # preenchimento da matriz
    for i in range(1, linhas):
        for j in range(1, colunas):
            # pega o valor do canto superior esquerdo e soma - se der igual pega a pontuação igual (match), se não, pega a pontuação diferente
            alinhar = matriz[i-1][j-1] + (igual if seq1[i-1] == seq2[j-1] else diferente) 
            # pega o valor acima e soma a pontuação da lacuna
            deletar = matriz[i-1][j] + lacuna
            # pega o valor da esquerda e soma a pontuação da lacuna
            inserir = matriz[i][j-1] + lacuna
            # coloca na matriz o maior valor entre 
            matriz[i][j] = max(alinhar, deletar, inserir)
    
    for j in matriz:
        print(j)

########################################################################################################

    # Rastreamento (Backtracking)
    alinhamento_1, dalinhamento_2 = "", "" # inicializa as variáveis de alinhamento 1 e 2

    # para cada linha de linhas e para cada coluna de colunas
    linha, coluna = linhas - 1, colunas - 1 
    
    # loop enquanto ambos os índices linha e coluna forem maiores que 0, o que significa que ainda não chegamos à borda superior ou à esquerda da matriz.
    while linha > 0 and coluna > 0: 
        
        # verifica se a pontuação atual na matriz é igual à pontuação da diagonal superior esquerda mais a pontuação correspondente ao caractere 
        # atual das duas sequências. Se for verdadeiro, significa que o caractere está alinhado (match ou mismatch).
        if matriz[linha][coluna] == matriz[linha-1][coluna-1] + (igual if seq1[linha-1] == seq2[coluna-1] else diferente): 
            
            # adiciona os caracteres correspondentes das sequências seq1 e seq2 às strings de alinhamento.
            alinhamento_1 = seq1[linha-1] + alinhamento_1
            dalinhamento_2 = seq2[coluna-1] + dalinhamento_2

            # move os índices linha e coluna para a posição da diagonal superior esquerda na matriz.
            linha -= 1
            coluna -= 1
        
        # verifica se a pontuação atual na matriz é igual à pontuação da célula acima mais a penalidade de lacuna. 
        # isso indica que foi introduzida uma lacuna na sequência seq1.
        elif matriz[linha][coluna] == matriz[linha-1][coluna] + lacuna:
            #Adiciona um caractere de lacuna à sequência seq1 e um caractere correspondente de seq2 à string de alinhamento.
            alinhamento_1 = seq1[linha-1] + alinhamento_1
            dalinhamento_2 = "-" + dalinhamento_2

            # move o índice linha, caminhando para cima na matriz
            linha -= 1
        
        # verifica se a pontuação atual na matriz é igual à pontuação da célula à esquerda mais a penalidade de lacuna. 
        # isso indica que foi introduzida uma lacuna na sequência seq2.
        else:
            # Adiciona um caractere de lacuna à sequência seq2 e um caractere correspondente de seq1 à string de alinhamento.
            alinhamento_1 = "-" + alinhamento_1
            dalinhamento_2 = seq2[coluna-1] + dalinhamento_2

            # move o índice coluna, caminhando para a esquerda na matriz
            coluna -= 1

########################################################################################################

    print("Resultado do alinhamento da sequência 1:", alinhamento_1)
    print("Resultado do alinhamento da sequência 2:", dalinhamento_2)

########################################################################################################

    # calculo da identidade do alinhamento
    seq1 = alinhamento_1
    seq2 = dalinhamento_2

    tam_seq = len(seq1)
    cont = 0

    for i in range(tam_seq):
        if seq1[i] == seq2[i]:
            cont = cont + 1
        
    # identidade: refere-se à presença do mesmo nucleotídeo ou aminoácido na mesma posição em duas sequências alinhadas
    identidade = cont/tam_seq*100
    print(f'Identidade: {identidade}%')

########################################################################################################

###################### COMECE AQUI #####################################################################

# abre o arquivo e extrai a primeira sequencia
arquivo = open('seq1.txt')
seq1 = arquivo.readline() #TGCTCGTA

# abre o arquivo e extrai a segunda sequencia
arquivo = open('seq2.txt')
seq2 = arquivo.readline() #TTCATA

# chama a função de programação dinâmica de Needleman Wunch
needleman_wunsch(seq1, seq2)

########################################################################################################
