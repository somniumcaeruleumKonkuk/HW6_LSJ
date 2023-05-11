#q1.py
import matplotlib.pyplot as plt
import csv

def q1():
    csv_labels = ['nationwide.csv','seoul.csv','daejeon.csv','busan.csv','jeju.csv']
    city_labels = ['NationWide', 'Seoul', 'Daejeon', 'Busan', 'Jeju']
    temp = [[],[],[],[],[]]
    colors = ['blue', 'skyblue', 'yellow', 'red', 'purple']

    plt.title('q1')
    months=[]
    for i in range(12):
        months += [i+1]
    city = 0
    for city in range(5):
        f = open(csv_labels[city], 'r', encoding='utf-8')
        data = csv.reader(f)
        
        for i in range(8):
            next(data)

        month=1
        for i in data:
            if month == 13:
                break
            try:
                temp[city] += [float(i[2])]
            except:
                temp[city] += [-100]
            finally:
                month = month + 1
                
        plt.plot(months, temp[city], color=colors[city], label = city_labels[city])
    plt.xticks(months, ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
                
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    q1()
