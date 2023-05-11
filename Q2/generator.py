#random number generator
def generator():
    import random
    import csv
    num = [100, 1000, 10000, 100000]
    for i in num:
        line = str()
        
        for j in range(int(i)):
            line += str(random.randint(1,6))

        f = open(str(i)+'.csv', 'w', encoding='utf-8')
        data = csv.writer(f)

        data.writerow(line)

if __name__=='__main__':
    generator()
