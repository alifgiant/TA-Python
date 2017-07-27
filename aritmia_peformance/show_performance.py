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

if __name__ == '__main__':
    real_100_count = {'1': 46102, '2': 1572, '3': 0}
    real_200_count = {'1': 52684, '2': 9335, '3': 472}

    '''...................select-source------------------------'''
    records = json.load(open('aritmia_ori.json'))
    # records = json.load(open('aritmia_modif.json'))
    '''...................select-source------------------------'''

    detect_100_count = Counter()
    detect_200_count = Counter()

    for record in records:
        if int(record) < 200:
            detect_100_count += Counter(records[record])
        else:
            detect_200_count += Counter(records[record])

    print(detect_100_count)
    print(detect_200_count)

    # normal = ConfusionMatrix(47668, 43462, 46102)
    # pc = ConfusionMatrix(47668, 2739, 1572)
    # f = ConfusionMatrix(47668, 0, 0)
    #
    # print('Series 100')
