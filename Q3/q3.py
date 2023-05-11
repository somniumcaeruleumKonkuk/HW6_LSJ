#q3.py
def q3():
    import matplotlib.pyplot as plt

    #Jeju
    f = open('ratio.csv', 'r', encoding='utf-8')
    
    f.readline()
    f.readline()

    years = list()
    for i in range(23):
        years.append(i+2000)
    
    L = str(f.readline()).split(',')
    l = list()

    for i in range(1, len(L), 3):
        l.append(float(L[i]))

    l.reverse()
    
    plt.plot(years, l, color='purple',label='Jeju')

    #Nationwide
    f = open('ratio_nationwide.csv', 'r', encoding='utf-8')
    
    f.readline()
    f.readline()

    years = list()
    for i in range(23):
        years.append(i+2000)
    
    L = str(f.readline()).split(',')
    l = list()

    for i in range(1, len(L), 3):
        l.append(float(L[i]))
    
    plt.plot(years, l, color='blue',label='Nationwide')

    #Print
    plt.legend()
    plt.title('Ratio of Gender')
    plt.show()
    
if __name__ == '__main__':
    q3()
