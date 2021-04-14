try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()


def question06():
    directory = './data/chromosome_position_data.txt'   # este é o diretório do dataset para esta questão,
                                                        # caso o seu dataset esteja em outro caminho
                                                        # informar nesta variável
    data = open(directory, 'r') # recuperando o conteúdo do dataset somente para leitura
    listColors = ['#e71c1e','#3f89c0', '#57b854']

    x = []
    mut1 = []
    mut2 = []
    WT = []

    for line in data:   # lendo cada linha do dataset e fazendo o devido tratamento para a geração do gráfico
        if line.split('\t')[0] != 'Position':
            aux = int(line.split('\t')[0])
            aux1 = float(line.split('\t')[1])
            aux2 = float(line.split('\t')[2])
            aux3 = float(line.split('\t')[3].split('\n')[0])

            x.append(aux)
            mut1.append(aux1)
            mut2.append(aux2)
            WT.append(aux3)

    plt.plot(x,mut1, color = listColors[0])
    plt.plot(x,mut2, color = listColors[1])
    plt.plot(x,WT, color = listColors[2])

    plt.yticks([0,10,20,30,40,50,60,70])
    plt.xticks([91758000,91760000,91762000,91764000,91766000])

    plt.xlabel('Position within chromosome')
    plt.ylabel('Value')

    plt.legend(['Mut1','Mut2','WT'],loc=2)
    plt.show()

question06()