
import pytest

from recycling_rewards import (
    reward_points,
    collection_accepted,
    slot_status
)


# Reward points tests

def test_unknown_material():
    with pytest.raises(ValueError):
        reward_points("glass", 10, False)


def test_negative_weight():
    with pytest.raises(ValueError):
        reward_points("paper", -1, False)


def test_bonus_applied():
    assert reward_points("paper", 4, True) == 0


def test_bonus_not_applied():
    assert reward_points("paper", 10, False) == 30


def test_metal_bonus_ignored():
    assert reward_points("metal", 5, True) == 36


def test_zero_extra_weight():
    assert reward_points("paper", 5, False) == 0


def test_normal_non_metal_rate():
    assert reward_points("plastic", 10, False) == 42


def test_normal_metal_rate():
    assert reward_points("metal", 4, False) == 24


def test_large_non_metal_weight():
    assert reward_points("paper", 30, False) == 250


def test_large_metal_weight():
    assert reward_points("metal", 25, False) == 414


# Collection acceptance tests

def test_hazardous_accepted():
    assert collection_accepted(5, 5, True) is True


def test_hazardous_rejected():
    assert collection_accepted(6, 2, True) is False


def test_non_hazardous_over_50():
    assert collection_accepted(51, 2, False) is False


def test_non_hazardous_within_limit():
    assert collection_accepted(30, 3, False) is True


def test_too_many_bags():
    assert collection_accepted(30, 4, False) is False


def test_exactly_50kg():
    assert collection_accepted(50, 3, False) is True


# Slot status tests

def test_morning_open():
    assert slot_status(20, True, False) == "open"


def test_evening_open():
    assert slot_status(10, False, False) == "open"


def test_morning_holiday_open():
    assert slot_status(35, True, True) == "open"


def test_evening_holiday_open():
    assert slot_status(25, False, True) == "open"


def test_morning_late():
    assert slot_status(10, True, False) == "late"


def test_evening_late():
    assert slot_status(5, False, False) == "late"


def test_holiday_late():
    assert slot_status(20, True, True) == "late"


def test_morning_missed():
    assert slot_status(4, True, False) == "missed"


def test_evening_missed():
    assert slot_status(-6, False, False) == "missed"


def test_holiday_missed():
    assert slot_status(19, True, True) == "missed"
