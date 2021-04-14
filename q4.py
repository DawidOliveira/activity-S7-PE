try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()


def question04():
    directory = './data/male_female_counts.txt' # este é o diretório do dataset para esta questão,
                                                # caso o seu dataset esteja em outro caminho
                                                # informar nesta variável
    data = open(directory, 'r') # recuperando o conteúdo do dataset somente para leitura
    listColors = ['#ff0000','#ffa300','#d2ff00','#3aff00','#00ff71','#00ffff','#0071ff','#3a00ff','#d200ff','#ff00a3']
    x = []
    y = []
    for line in data:   # lendo cada linha do dataset e fazendo o devido tratamento para a geração do gráfico
        if line.split('\t')[0] != 'Sample':
            x.append(line.split('\t')[0])
            y.append(int(line.split('\t')[1].split('\n')[0]))


    plt.figure(figsize=(10,6))
    plt.bar(x, y, color = listColors)

    plt.yticks([0,5,10,15])

    plt.show()

question04()