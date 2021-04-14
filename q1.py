try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()

def question01():
    directory = './data/weight_chart.txt'   # este é o diretório do dataset para esta questão,
                                            # caso o seu dataset esteja em outro caminho
                                            # informar nesta variável

    data = open(directory, 'r') # recuperando o conteúdo do dataset somente para leitura
    x = []
    y = []
    for line in data: # lendo cada linha do dataset e fazendo o devido tratamento para a geração do gráfico
        if line.split('\t')[0] != 'Age':
            x.append(int(line.split('\t')[0]))
            y.append(float(line.split('\t')[1].split('\n')[0]))
        


    plt.plot(x, y, marker = 'o', markerfacecolor='white')
    plt.xticks([0,2,4,6,8])
    plt.yticks([2,4,6,8,10])
    plt.xlabel('Age (months)')
    plt.ylabel('Weight (kg)')
    plt.title('The relationship between age and weight in a growing infant')

    plt.show()

question01()