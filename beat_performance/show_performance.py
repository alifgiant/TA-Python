def process(address):
    file_result = open(address)

    records = []
    temp = dict()
    for idx, line in enumerate(file_result):
        if idx % 4 == 0:
            temp = dict()
            temp['num'] = int(line)
        elif idx % 4 == 1:
            temp['duration'] = float(line[5:-12])
        elif idx % 4 == 3:
            data = line.split(' ')
            temp['acc'] = float(data[1])
            temp['sp'] = float(data[4])
            temp['se'] = float(data[6][:-1])

            records.append(temp)
    return records


def average(records):
    series100 = {'acc': 0, 'se': 0, 'sp': 0, 'duration': 0, 'count': 0}
    series200 = {'acc': 0, 'se': 0, 'sp': 0, 'duration': 0, 'count': 0}

    for record in records:
        if record['num'] < 200:
            series = series100
        else:
            series = series200

        series['count'] += 1
        series['acc'] += record['acc']
        series['se'] += record['se']
        series['sp'] += record['sp']
        series['duration'] += record['duration'] / 650000  # total signal length, avg per beat

    for key in series100:
        if key != 'count':
            series100[key] /= series100['count']
    for key in series200:
        if key != 'count':
            series200[key] /= series200['count']

    print('series 100', series100)  # show
    print('series 200', series200)  # show

if __name__ == '__main__':
    original_address1 = 'performance_ori1.txt'
    original_address2 = 'performance_ori2.txt'

    modified_address1 = 'perform01.txt'
    modified_address2 = 'perform02.txt'
    modified_address3 = 'performance_modif.txt'
    modified_address4 = 'perform04.txt'
    modified_address5 = 'perform05.txt'

    ori1 = process(original_address1)
    ori2 = process(original_address2)

    modified1 = process(modified_address1)
    modified2 = process(modified_address2)
    modified3 = process(modified_address3)
    modified4 = process(modified_address4)
    modified5 = process(modified_address5)

    # print(ori[0])
    # print(modified[0])

    print('----------ori-01---------')
    average(ori1)
    print('----------ori-02---------')
    average(ori2)
    
    print('---------modif-01--------')
    average(modified1)
    print('---------modif-02--------')
    average(modified2)
    print('---------modif-03--------')
    average(modified3)
    print('---------modif-04--------')
    average(modified4)
    print('---------modif-05--------')
    average(modified5)
