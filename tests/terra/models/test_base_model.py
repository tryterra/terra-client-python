import itertools

from terra import models


def peek(iterable):
    try:
        first = next(iterable)
    except StopIteration:
        return None
    return first, itertools.chain([first], iterable)


def test_filter():

    filtered = models.v2.activity.Activity().filter_data("heart")
    k = peek(filtered)
    assert k is not None


def test_get_attr():

    l = [
        "metadata",
        "lap_data",
        "distance_data",
        "position_data",
        "active_durations_data",
        "active_durations_data",
        "MET_data",
        "movement_data",
        "calories_data",
        "work_data",
        "power_data",
    ]

    for z in l:
        assert z in models.v2.activity.Activity().keys()
