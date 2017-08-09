import time
import json
import CsvLoader
import sample
from algo.filter import Filter

from algo import original_pantom  # original
from algo import modif_pantom  # modified
from algo.helper import ConfusionMatrix


def beat_loc_and_signal(address, begin, end):
    file_beat = json.load(open(address + '/beat_loc.json'))[begin:end]

    # raw = CsvLoader.load_dummy(1)
    file_raw = CsvLoader.load(address + '/record.csv')[begin:end]

    return file_beat, file_raw


def do_preprocessing(raw_signal):
    # filtering
    low_high_filter = Filter('coef/coef-filter.json')
    filtered = []
    for x in raw_signal:
        filtered.append(low_high_filter.execute(x))

    # derivative
    der_filter = Filter('coef/coef-derr.json')
    der = []
    for x in filtered:
        der.append(der_filter.execute(x))

    squared = []
    for x in der:
        squared.append(x ** 2)

    # MWI
    mwi_filter = Filter('coef/coef-mwi.json')
    mwi = []
    for x in squared:
        mwi.append(mwi_filter.execute(x))

    # print(mwi)

    # REMOVED DELAY
    # print('delay', low_high_filter.get_delay()+der_filter.get_delay()+mwi_filter.get_delay())
    removed = mwi[int(low_high_filter.get_delay() + der_filter.get_delay() + mwi_filter.get_delay()):]

    return removed


def do_original_algorithm(raw_signal):
    removed = do_preprocessing(raw_signal)

    # detector = BeatDetector(360, window_duration=2.2, val_by_mean=1.1, idx_by_r=0.72)
    detector = original_pantom.BeatDetector(360, chunk_size_by_freq=0.2, init_duration=8, threshold_by_mean=1.1)
    peaks = []
    thrs = []

    for x in removed:
        res = detector.detect(x)
        if res and len(res) > 1:
            peak, thr = res
            peaks += peak
            thrs += thr

    peaks += [0] * len(detector.search_back_sample)
    thrs += [0] * len(detector.search_back_sample)

    return peaks


def do_modified_algorithm(raw_signal):
    removed = do_preprocessing(raw_signal)

    # detector = modif_pantom.BeatDetector(360, window_duration=8, val_by_mean=1.1, idx_by_r=0.8)
    # detector = modif_pantom.BeatDetector(360, window_duration=7, val_by_mean=1.1, idx_by_r=0.8)
    detector = modif_pantom.BeatDetector(360, window_duration=6.5, val_by_mean=1.1, idx_by_r=0.8)
    # detector = modif_pantom.BeatDetector(360, window_duration=6.5, val_by_mean=0.65, idx_by_r=0.87)
    # detector = modif_pantom.BeatDetector(360, window_duration=6.5, val_by_mean=0.65, idx_by_r=0.93)

    peaks = []
    thrs = []

    for x in removed:
        res = detector.detect(x)
        if res and len(res) > 1:
            peak, thr = res
            peaks += peak
            thrs += thr

    # peaks += [0] * len(detector.search_back_sample)
    # thrs += [0] * len(detector.search_back_sample)

    # execute what left in buffer
    res = detector.execute_buffer()

    if res and len(res) > 1:
        peak, thr = res
        peaks += peak
        thrs += thr

    return peaks

if __name__ == '__main__':
    source = sample.MitBih
    base = sample.MitBih.base

    '''..........................Select Source.................................'''
    records = source.get_all_record()  # all records
    # records = source.get_one_record(num=100)      # record number 100
    # records = source.get_record_series_100()      # 100s records
    # records = source.get_record_series_200()      # 200s records
    '''........................................................................'''

    '''..........................Select Start Stop.................................'''
    start, stop = 0, None       # All Record
    # start, stop = 0, 2935       # First 8 second
    # start, stop = 10000, 20000  # Custom
    # start, stop = -2935, None   # Last 8 second
    '''..........................Select Start Stop.................................'''

    for record in records:
        for x in range(10):  # 10 experiment            
            str_record = str(record)
            print(str_record)

            record_address = base + '/' + str_record

            '''.............................Load Data....................................'''
            beat, raw = beat_loc_and_signal(record_address, start, stop)

            start_time = time.time()
            '''..........................Select Detector.................................'''
            # detected_peaks = do_original_algorithm(raw)
            detected_peaks = do_modified_algorithm(raw)
            '''..........................Select Detector.................................'''
            stop_time = time.time()
            print("--- %s seconds ---" % (stop_time - start_time))

            real = beat.count(1)
            detect = detected_peaks.count(0.5)

            # output = open(number + '/result.txt', 'w')
            # print('beat in real', real, file=output)
            # print('beat in detected', detect, file=output)
            # print('beat missed |x|', abs(real-detect), file=output)
            # print('accuracy', 100 * (detect / real), '%', file=output)
            # print('missed', 100 * (abs(detect-real) / real), '%', file=output)
            # print('finished:', number, '|', 'accuracy:', 100 * (detect / real), '%')
            mat = ConfusionMatrix(len(beat), detect, real)
            print('ex:', x, '|', 'finished:', record_address, '|', 'length:', len(beat),  'real:', real, 'detected:', detect)
            print('acc:', mat.get_accuracy(), '%', 'sp:', mat.get_specificity(), 'se:', mat.get_recall())
            # output.close()

            '''..............................Exactly at Same Loc Acc................................'''
            # peaks = peaks[2:]
            # same = 0
            # for x, y in zip(beat, peaks):
            #     if (x == 1 and y == 0.5):
            #         same += 1
            # print('same:', same, 'len-beat', len(beat), 'len-peak', len(peaks))
            '''..............................Exactly at Same Loc Acc................................'''

            '''..............................Wave Plotter....................................'''
            # import matplotlib.pyplot as plt
            # fig, (ax_raw, ax_filtered, ax_der, ax_squared, ax_mwi, ax_peaks) = plt.subplots(6, 1)
            
            # ax_raw.plot(raw)
            # ax_raw.plot(beat)
            # ax_filtered.plot(filtered)
            # ax_der.plot(der)
            # ax_squared.plot(squared)
            # ax_mwi.plot(mwi)
            # # ax_peaks.plot(raw)
            # ax_peaks.plot(removed)
            # ax_peaks.plot(beat)
            # ax_peaks.plot(peaks)
            # # ax_peaks.plot(search_back_peak)
            
            # plt.tight_layout()
            # plt.show()
            '''..............................Wave Plotter....................................'''
