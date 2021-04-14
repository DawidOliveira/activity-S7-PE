try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()


def question02():
    directory = './data/feature_count.txt'  # este é o diretório do dataset para esta questão,
                                            # caso o seu dataset esteja em outro caminho
                                            # informar nesta variável
    data = open(directory, 'r') # recuperando o conteúdo do dataset somente para leitura
    x = []
    y = []
    for line in data:   # lendo cada linha do dataset e fazendo o devido tratamento para a geração do gráfico
        if line.split('\t')[0] != 'Feature':
            x.append(line.split('\t')[0])
            y.append(int(line.split('\t')[1].split('\n')[0]))
        
    plt.figure(figsize=(18,5))
    plt.barh(x, y)
    plt.xlabel('Number of features')

    plt.show()

question02()