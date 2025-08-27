import numpy as np

def median_R(data):
    n = len(data)
    sorted_data = sorted(data) 

    if n  % 2 == 0: # % symbol returns the part that’s left over after dividing one number by another
        median = sorted_data[n // 2] 
    else:
        mid_1 = sorted_data[ n // 2-1] #could also be 2+1
        mid_2 = sorted_data[n // 2]
        median = (mid_1 + mid_2) / 2

    return median


def frequency_R(data):

    '''gives back: max_mode, max_frequency, min_mode, min_frequency'''

    frequency_dict = {}
    for item in data:
        if item in frequency_dict:
            frequency_dict[item] += 1 # item is already in the dictionary
        else:
            frequency_dict[item] = 1 # new item

    max_mode = None # in case of errors in the dataset
    min_mode = None
    max_frequency = 0
    min_frequency = float('inf')

    for item, frequency in frequency_dict.items(): # items in dictionary: {'Manhattan': 1}
        if frequency > max_frequency:
            max_frequency = frequency
            max_mode = item

    for item, frequency in frequency_dict.items(): # items in dictionary: {'Manhattan': 1}
        if frequency < min_frequency:
            min_frequency = frequency
            min_mode = item


    return max_mode, max_frequency, min_mode, min_frequency