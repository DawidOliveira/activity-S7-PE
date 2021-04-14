try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\npip3 install matplotlib')
    exit()

try:
    import numpy as np
except ImportError:
    print('você não tem o numpy instalado, por favor execute o seguinte comando:\npip install numpy\n\nor\npip3 install numpy')
    exit()


def question01():
    data = open('./data/weight_chart.txt', 'r')
    x = []
    y = []
    for line in data:
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

def question02():
    data = open('./data/feature_count.txt', 'r')
    x = []
    y = []
    for line in data:
        if line.split('\t')[0] != 'Feature':
            x.append(line.split('\t')[0])
            y.append(int(line.split('\t')[1].split('\n')[0]))
        
    plt.figure(figsize=(18,5))
    plt.barh(x, y)
    plt.xlabel('Number of features')

    plt.show()

def question03():
    data1 = np.random.normal(size=10000, loc=0)
    data2 = np.random.normal(size=10000, loc=4)
    data = np.concatenate([data1, data2])
    plt.hist(data, bins=110, facecolor='#ffffff', edgecolor='k')
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plt.show()

def question04():
    data = open('./data/male_female_counts.txt', 'r')
    listColors = ['#ff0000','#ffa300','#d2ff00','#3aff00','#00ff71','#00ffff','#0071ff','#3a00ff','#d200ff','#ff00a3']
    x = []
    y = []
    for line in data:
        if line.split('\t')[0] != 'Sample':
            x.append(line.split('\t')[0])
            y.append(int(line.split('\t')[1].split('\n')[0]))


    plt.figure(figsize=(10,6))
    plt.bar(x, y, color = listColors)

    plt.yticks([0,5,10,15])

    plt.show()

def question05():
    data = open('./data/up_down_expression.txt', 'r')
    listColors = ['#f00000','#0000f0', '#c5c5c5']
    for line in data:
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

def question06():
    data = open('./data/chromosome_position_data.txt', 'r')
    listColors = ['#e71c1e','#3f89c0', '#57b854']

    x = []
    mut1 = []
    mut2 = []
    WT = []

    for line in data:
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

def question07():
    data = open('./data/brain_bodyweight.txt', 'r')
    plt.figure(figsize=(10,5))

    for line in data:
        if line.split('\t')[0] != 'Species ' and line.split('\t')[0] != 'Species':
            aux = line.split('\t')[0]
            aux1 = float(line.split('\t')[1])
            aux2 = float(line.split('\t')[2])
            aux3 = float(line.split('\t')[3])
            aux4 = float(line.split('\t')[4].split('\n')[0])
            
            print(aux, aux1, aux2, aux3, aux4)

            plt.scatter(aux2,aux1,color = "#000000",marker='.')
            plt.text(aux2 - .1,aux1 - .3,s=aux,fontdict=dict(size=8))
            plt.errorbar(aux2,aux1,xerr=aux4,yerr=aux3,fmt='*',ecolor="#000000", mfc="#000000",mec="#000000", capsize=4)
    plt.xticks([0,1,2,3])
    plt.yticks([-1,0,1,2,3,4,5])

    plt.xlabel('Brain weight')
    plt.ylabel('Body weight')

    plt.show()

question01()

question02()

question03()

question04()

question05()

question06()

question07()
