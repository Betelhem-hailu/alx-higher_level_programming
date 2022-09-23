<<<<<<< HEAD
#!/usr/bin/python3
"""find the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function that accepts a list and finds the peak """
    if list_of_integers is None or list_of_integers == []:
        return (None)
    return (do_find_peak(list_of_integers, 0, len(list_of_integers)))


def do_find_peak(lst, l, e):
    """ really find the peak where the first & last index given """

    m = int((l + e) / 2)
    h = e - 1
    if ((m == 0 or lst[m] >= lst[m - 1]) and (m == h or lst[m] >= lst[m + 1])):
        return lst[m]
    elif (m > 0 and lst[m - 1] > lst[m]):
        return do_find_peak(lst, l, m - 1)
    else:
        return do_find_peak(lst, m + 1, e)
=======
#!/usr/bin/python3
""" contains find_peak """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if (not list_of_integers):
        return None
    if (len(list_of_integers) <= 2):
        return max(list_of_integers)
    peak = None
    if (list_of_integers[0] >= list_of_integers[1]):
        peak = list_of_integers[0]
    if (list_of_integers[-1] >= list_of_integers[-2]):
        peak = list_of_integers[-1]
    if (peak):
        return peak
    i = 1
    while (i < len(list_of_integers) - 1):
        if (list_of_integers[i] >= list_of_integers[i + 1] and
                list_of_integers[i] >= list_of_integers[i - 1]):
            return list_of_integers[i]
        else:
            i += 1
    return peak
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
