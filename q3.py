try:
    import matplotlib.pyplot as plt
except ImportError:
    print('você não tem o matplotlib instalado, por favor execute o seguinte comando:\npip install matplotlib\n\nor\n\npip3 install matplotlib')
    exit()

try:
    import numpy as np
except ImportError:
    print('você não tem o numpy instalado, por favor execute o seguinte comando:\npip install numpy\n\nor\n\npip3 install numpy')
    exit()


def question03():
    data1 = np.random.normal(size=10000, loc=0)
    data2 = np.random.normal(size=10000, loc=4)
    data = np.concatenate([data1, data2])
    plt.hist(data, bins=110, facecolor='#ffffff', edgecolor='k')
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plt.show()

question03()