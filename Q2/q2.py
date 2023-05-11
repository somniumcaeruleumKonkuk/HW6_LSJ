#q2.py

def q2():
    import matplotlib.pyplot as plt
    csv_names = ['100', '1000', '10000', '100000']

    figure, axis = plt.subplots(2,2)
    
    for i in range(4):
        f = open(csv_names[i]+'.csv', 'r', encoding='utf-8')
        line = str(f.readline()).split(',')
        line.sort()

        l = list()

        for j in line:
             l.append(int(j))
        
        axis[int(i/2), i%2].hist(l, bins = 6)
        axis[int(i/2), i%2].set_title(str(csv_names[i]))

    plt.show()

if __name__ == "__main__":
    q2()
