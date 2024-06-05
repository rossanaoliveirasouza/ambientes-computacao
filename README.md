## Este é um trabalho apresentado à disciplina de Ambientes em Computação do Programa de Pós Graduação em Bioinformática da Universidade Federal de Minas Gerais (UFMG)
Alunos: Fabiano Santana, Helena L. Costa, Rossana O. Souza e Thaiane G. Nascimento
Algoritmo implementado: Algoritmo de sequênciamento de Needleman Wunch  

## Como baixar e rodar o repositório

Para baixar e rodar o repositório, siga os seguintes passos:

Clone o repositório usando o comando: git clone <URL_do_repositório>.  
Navegue até o diretório do repositório clonado: cd <nome_do_repositório>.  
Certifique-se de que você possui o Python instalado. Para rodar o programa, utilize o comando:  
```sh 
python needleman_wunsch.py
```
## Funcionamento do algoritmo
O algoritmo em questão foi proposto na década de 1970 por Saul Needleman e Christian Wunsch. Ele tem como principal função o alinhamento global entre um par de sequências. Para iniciar esse  algoritmo é criada uma matriz mxn, onde m é o tamanho da primeira sequência e n é o tamanho da segunda sequência a ser alinhada. 
Na matriz, cada célula representa a pontuação do alinhamento entre as subsequências das duas sequências que estão sendo comparadas. As bordas da matriz são inicializadas com pontuações de gap. Isso representa o custo de inserir e deletar para alinhar as sequências. O restante da matriz  é preenchido calculando a pontuação de cada célula com base em três possíveis movimentos:

* Match: Comparação entre os caracteres correspondentes das duas sequências. Se forem iguais, a pontuação é aumentada.
* Mismatch: Comparação entre os caracteres correspondentes das duas sequências. Se forem diferentes, a pontuação é diminuída.
* Gap: Introdução de um gap (inserção ou deleção) em uma das sequências. Isso aumenta a pontuação.
  
Dessa forma, a matriz de pontuação é preenchida com valores que representam a similaridade entre as subsequências das duas sequências que estão sendo comparadas. Cada célula contém a pontuação do melhor alinhamento entre as subsequências até essa posição. Após preencher a matriz, rastreamos de volta da célula inferior direita até a célula superior esquerda para encontrar o caminho ótimo. Durante o rastreamento, registramos as operações realizadas (match, mismatch, gap) para construir o alinhamento das duas sequências.
