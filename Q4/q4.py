#q4.py
def q4():
    import csv
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams['font.family'] = 'Malgun Gothic'

    f = open('stations.csv', 'r', encoding='utf-8')
    data = csv.reader(f)

    next(data)
    next(data)
    
    stations = dict() #[0]: 승차, [1]: 하차

    for i in data:
        try:
            station_name = str(i[3]).strip()
            if station_name in stations.keys():
                stations[station_name][0] += int(i[10].replace('"', '').replace(',','').strip()) + int(i[12].replace('"', '').replace(',','').strip())
                stations[station_name][1] += int(i[11].replace('"', '').replace(',','').strip()) + int(i[13].replace('"', '').replace(',','').strip())

            else:
                stations[station_name] = [int(i[10].replace('"', '').replace(',','').strip()) + int(i[12].replace('"', '').replace(',','').strip()), int(i[11].replace('"', '').replace(',','').strip()) + int(i[13].replace('"', '').replace(',','').strip())]

        except IndexError:
            pass
    
    #최대 승차역 30개
    stations_geton = list(stations.keys())
    l_geton = []
    for i in range(len(stations_geton)-1):
        for j in range(i+1, len(stations_geton)): #내림차순(descending)
            num_previous = stations[str(stations_geton[i])][0]
            num_next = stations[str(stations_geton[j])][0]

            if num_previous > num_next:
                pass
            elif num_previous == num_next:
                if j+1 == len(stations_geton):
                    stations_geton = stations_geton[:i+1] + [stations_geton[j]] + stations_geton[i+1:j]
                else:
                    stations_geton = stations_geton[:i+1] + [stations_geton[j]] + stations_geton[i+1:j] + stations_geton[j+1:]
            else:
                #swap(stations_get[i], stations_get[j])
                tmp = stations_geton[i]
                stations_geton[i] = stations_geton[j]
                stations_geton[j] = tmp

    for i in stations_geton:
        l_geton.append(stations[i][0])

    #최대 하차역 30개
    stations_getoff = list(stations.keys())
    l_getoff = []
    for i in range(len(stations_getoff)-1):
        for j in range(i+1, len(stations_getoff)): #내림차순(descending)
            if stations[stations_getoff[i]][1] > stations[stations_getoff[j]][1]:
                pass
            elif stations[stations_getoff[i]][1] == stations[stations_getoff[j]][1]:
                if j+1 == len(stations_getoff):
                    stations_getoff = stations_getoff[:i+1] + [stations_getoff[j]] + stations_getoff[i+1:j]
                else:
                    stations_getoff = stations_getoff[:i+1] + [stations_getoff[j]] + stations_getoff[i+1:j] + stations_getoff[j+1:]
            else:
                #swap(stations_get[i], stations_get[j])
                tmp = stations_getoff[i]
                stations_getoff[i] = stations_getoff[j]
                stations_getoff[j] = tmp

    for i in stations_getoff:
        l_getoff.append(stations[i][1])

    #최대 승하차역 30개
    stations_get = list(stations.keys())
    l_get = []
    for i in range(len(stations_get)-1):
        for j in range(i+1, len(stations_get)): #내림차순(descending)
            num_previous = int(stations[str(stations_get[i])][0]) + int(stations[str(stations_get[i])][1])
            num_next = int(stations[str(stations_get[j])][0]) + int(stations[str(stations_get[j])][1])

            if num_previous > num_next:
                pass
            elif num_previous == num_next:
                if j+1 == len(stations_get):
                    stations_get = stations_get[:i+1] + [stations_get[j]] + stations_get[i+1:j]
                else:
                    stations_get = stations_get[:i+1] + [stations_get[j]] + stations_get[i+1:j] + stations_get[j+1:]
            else:
                #swap(stations_get[i], stations_get[j])
                tmp = stations_get[i]
                stations_get[i] = stations_get[j]
                stations_get[j] = tmp
    
    for i in stations_get:
        l_get.append(int(stations[i][0]) + int(stations[i][1]))
    

    #그래프 출력
    plt.figure().set_figwidth(10000)
    X_axis = np.arange(30)

    FONTSIZE = 3.9
    LABELSIZE = 6

    #승차역
    plt.subplot(3,1,1)
    plt.bar(X_axis - 0.2, l_geton[:30], 0.5)

    for i in range(len(stations_geton)):
        if(len(stations_geton[i]) > 5):
            stations_geton[i] = str(stations_geton[i][:5]) + '\n' + str(stations_geton[i][5:])

    plt.xticks(X_axis, stations_geton[:30], fontsize = FONTSIZE)
    plt.ylabel('승차역', fontsize=LABELSIZE)


    #하차역
    plt.subplot(3,1,2)
    plt.bar(X_axis, l_getoff[:30], 0.5)

    for i in range(len(stations_getoff)):
        if(len(stations_getoff[i]) > 5):
            stations_getoff[i] = str(stations_getoff[i][:5]) + '\n' + str(stations_getoff[i][5:])

    plt.xticks(X_axis, stations_getoff[:30], fontsize = FONTSIZE)
    plt.ylabel('하차역', fontsize=LABELSIZE)


    #승하차역
    plt.subplot(3,1,3)
    plt.bar(X_axis + 0.2, l_get[:30], 0.5)

    for i in range(len(stations_get)):
        if(len(stations_get[i]) > 5):
            stations_get[i] = str(stations_get[i][:5]) + str('\n') + str(stations_get[i][5:])

    plt.xticks(X_axis, stations_get[:30], fontsize = FONTSIZE)
    plt.ylabel('승하차역', fontsize=LABELSIZE)

    plt.legend()
    plt.show()

if __name__ == '__main__':
    q4()