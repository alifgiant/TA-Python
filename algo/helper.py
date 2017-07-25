
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
    pass
