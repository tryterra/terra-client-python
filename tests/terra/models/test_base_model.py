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
    attrs = [
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

    for attr in attrs:
        assert attr in models.v2.activity.Activity().keys()
