try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()


def question07():
    directory = './data/brain_bodyweight.txt'   # este é o diretório do dataset para esta questão,
                                                # caso o seu dataset esteja em outro caminho
                                                # informar nesta variável
    data = open(directory, 'r') # recuperando o conteúdo do dataset somente para leitura
    plt.figure(figsize=(10,5))

    for line in data:   # lendo cada linha do dataset e fazendo o devido tratamento para a geração do gráfico
        if line.split('\t')[0] != 'Species ' and line.split('\t')[0] != 'Species':
            aux = line.split('\t')[0]
            aux1 = float(line.split('\t')[1])
            aux2 = float(line.split('\t')[2])
            aux3 = float(line.split('\t')[3])
            aux4 = float(line.split('\t')[4].split('\n')[0])
            
            plt.scatter(aux2,aux1,color = "#000000",marker='.')
            plt.text(aux2 - .1,aux1 - .3,s=aux,fontdict=dict(size=8))
            plt.errorbar(aux2,aux1,xerr=aux4,yerr=aux3,fmt='*',ecolor="#000000", mfc="#000000",mec="#000000", capsize=4)
    plt.xticks([0,1,2,3])
    plt.yticks([-1,0,1,2,3,4,5])

    plt.xlabel('Brain weight')
    plt.ylabel('Body weight')

    plt.show()

question07()