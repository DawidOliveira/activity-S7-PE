try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()


def question05(): # esta questão tende a demorar para plotar o gráfico devido a grande quantidade de dados a serem analisados
    directory = './data/up_down_expression.txt' # este é o diretório do dataset para esta questão,
                                                # caso o seu dataset esteja em outro caminho
                                                # informar nesta variável
    data = open(directory, 'r') # recuperando o conteúdo do dataset somente para leitura
    listColors = ['#f00000','#0000f0', '#c5c5c5']
    for line in data:   # lendo cada linha do dataset e fazendo o devido tratamento para a geração do gráfico
        if line.split('\t')[0] != 'Gene':
            x = float(line.split('\t')[1])
            y = float(line.split('\t')[2])
            state = line.split('\t')[3].split('\n')[0]
            if(state == 'unchanging'):
                plt.scatter(x, y, color = listColors[2], marker='o')
            elif (state == 'up'):
                plt.scatter(x, y, color = listColors[0], marker='o')
            else:
                plt.scatter(x, y, color = listColors[1], marker='o')
    

    plt.yticks([0,5,10])
    plt.xticks([0,5,10])

    plt.xlabel('Condition 1')
    plt.ylabel('Condition 2')


    plt.show()

question05()