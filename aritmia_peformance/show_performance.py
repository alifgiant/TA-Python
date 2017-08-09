import json
from collections import Counter


class ConfusionMatrix(object):
    def __init__(self, total_length, detected, real):
        # input value
        self.total = total_length
        self.predicted_yes = detected
        self.predicted_no = total_length - detected
        self.actual_yes = real
        self.actual_no = total_length - real

        self.TP = detected if real > detected else real
        self.FP = detected - self.TP
        self.FN = real - self.TP
        self.TN = self.predicted_no - self.FN
        # print(self.TP, self.TN, self.FP, self.FN, self.actual_no)

    def get_accuracy(self):
        return 100 * ((self.TP + self.TN) / self.total)

    def get_specificity(self):
        return 100 * (self.TN / self.actual_no)

    def get_recall(self):
        return 100 * (self.TP / self.actual_yes)


def add_one(count, total):
    for key in count:
        count[key] += 1

    total += len(count.keys())

    return count, total

if __name__ == '__main__':
    real_100_count = {'1': 46117, '2': 1551, '3': 0}
    total_100 = 47668
    real_100_count, total_100 = add_one(real_100_count, total_100)

    real_200_count = {'1': 52856 '2': 9163, '3': 472}
    total_200 = 62491
    real_200_count, total_200 = add_one(real_200_count, total_200)

    '''...................select-source------------------------'''
    # records = json.load(open('aritmia_ideal.json'))
    # records = json.load(open('aritmia_ori.json'))
    records = json.load(open('aritmia_modif.json'))
    '''...................select-source------------------------'''

    detect_all_count = Counter()
    detect_100_count = Counter()
    detect_200_count = Counter()

    # for record in ['201']:
    for record in sorted(records):
        count = Counter(records[record])
        # print(record, count, sum(count.values()))
        detect_all_count += count
        if int(record) < 200:
            detect_100_count += count
        else:
            detect_200_count += count

    print('----ALL----', detect_all_count)
    print('----100----', detect_100_count)
    print('----200----', detect_200_count)

    '''..................................Confusion-100-series.................................'''
    normal_100 = ConfusionMatrix(total_100, detect_100_count['1']+1, real_100_count['1'])  # matrix 1
    pc_100 = ConfusionMatrix(total_100, detect_100_count['2']+1, real_100_count['2'])  # matrix 2
    f_100 = ConfusionMatrix(total_100, detect_100_count['3']+1, real_100_count['3'])  # matrix 3
    '''..................................Confusion-100-series.................................'''

    '''..................................Confusion-200-series.................................'''
    normal_200 = ConfusionMatrix(total_200, detect_200_count['1']+1, real_200_count['1'])  # matrix 1
    pc_200 = ConfusionMatrix(total_200, detect_200_count['2']+1, real_200_count['2'])  # matrix 2
    f_200 = ConfusionMatrix(total_200, detect_200_count['3']+1, real_200_count['3'])  # matrix 3
    '''..................................Confusion-200-series.................................'''

    print('===================')
    print('===================')

    print('------normal-------')
    print('acc:', normal_100.get_accuracy(), '%', 'sp:', normal_100.get_specificity(), 'se:', normal_100.get_recall())
    print('acc:', normal_200.get_accuracy(), '%', 'sp:', normal_200.get_specificity(), 'se:', normal_200.get_recall())
    print('------pc-----------')
    print('acc:', pc_100.get_accuracy(), '%', 'sp:', pc_100.get_specificity(), 'se:', pc_100.get_recall())
    print('acc:', pc_200.get_accuracy(), '%', 'sp:', pc_200.get_specificity(), 'se:', pc_200.get_recall())
    print('------f------------')
    print('acc:', f_100.get_accuracy(), '%', 'sp:', f_100.get_specificity(), 'se:', f_100.get_recall())
    print('acc:', f_200.get_accuracy(), '%', 'sp:', f_200.get_specificity(), 'se:', f_200.get_recall())


