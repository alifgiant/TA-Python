from collections import Counter
import sample
import main_beat
from algo.modif_pantom import ArrhythmiaDetector


def get_r_distance(peaks_list):
    last_idx = 0
    for idx, val in enumerate(peaks_list):
        if val == 0.5:
            yield (idx - last_idx)
            last_idx = idx


def turn_to_half(beats):
    return [beat/2 for beat in beats]

if __name__ == '__main__':
    source = sample.MitBih
    base = sample.MitBih.base

    '''..........................Select Source.................................'''
    # records = source.get_all_record()  # all records
    records = source.get_one_record(num=106)      # record number 100
    # records = source.get_record_series_100()      # 100s records
    # records = source.get_record_series_200()      # 200s records
    '''........................................................................'''

    '''..........................Select Start Stop.................................'''
    start, stop = 0, None  # All Record
    # start, stop = 0, 2935       # First 8 second
    # start, stop = 10000, 20000  # Custom
    # start, stop = -2935, None   # Last 8 second
    '''..........................Select Start Stop.................................'''

    all_occurrence = dict()
    for record in records:
        str_record = str(record)
        print(str_record)

        record_address = base + '/' + str_record

        beat_locs, raw = main_beat.beat_loc_and_signal(record_address, start, stop)
        print(Counter(beat_locs))

        '''..........................Select Detector.................................'''
        # print(detected_peaks  # test real
        # detected_peaks = turn_to_half(beat_locs)

        # detected_peaks = main_beat.do_original_algorithm(raw)
        detected_peaks = main_beat.do_modified_algorithm(raw)
        '''..........................Select Detector.................................'''

        arrhythmiaDetector = ArrhythmiaDetector(360)
        r_distance = list(get_r_distance(detected_peaks))
        beat_classes = arrhythmiaDetector.detect(r_distance)

        print('r_distance', r_distance)

        loc = list()
        for x, y in enumerate(beat_classes):
            if (y == 2): loc.append(x)

        print(loc)

        # print(len(beat_classes), 'asasasa')

        # assume first and last is normal
        beat_classes = [1] + beat_classes + [1]

        count = Counter(beat_classes)
        # all_occurrence_counter += count

        print(record_address, count)
        all_occurrence[str_record] = count

    # main_beat.json.dump(all_occurrence, open('aritmia_ideal.json', 'w'))
    # main_beat.json.dump(all_occurrence, open('aritmia_ori.json', 'w'))
    # main_beat.json.dump(all_occurrence, open('aritmia_modif.json', 'w'))
