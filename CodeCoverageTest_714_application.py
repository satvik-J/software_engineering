
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


def test_bonus_for_paper():
    assert reward_points("paper", 4, True) == 0


def test_no_bonus_for_plastic():
    assert reward_points("plastic", 5, False) == 12


def test_metal_rewards():
    assert reward_points("metal", 5, True) == 36


def test_extra_weight_above_20():
    assert reward_points("paper", 30, False) == 250


def test_metal_extra_weight_above_20():
    assert reward_points("metal", 25, False) == 414


# Collection acceptance tests

def test_hazardous_collection_accepted():
    assert collection_accepted(5, 5, True) is True


def test_hazardous_collection_rejected():
    assert collection_accepted(6, 2, True) is False


def test_collection_above_50kg():
    assert collection_accepted(51, 2, False) is False


def test_collection_within_limits():
    assert collection_accepted(30, 2, False) is True


# Slot status tests

def test_morning_slot_open():
    assert slot_status(20, True, False) == "open"


def test_evening_slot_late():
    assert slot_status(5, False, False) == "late"


def test_holiday_slot_open():
    assert slot_status(35, True, True) == "open"


def test_slot_missed():
    assert slot_status(-6, False, False) == "missed"
