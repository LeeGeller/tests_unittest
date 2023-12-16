import pytest

from utils.dicts import get_val


def test_get_val_valid(fixture_dict):
    assert get_val(fixture_dict, 'name') == 'Kris'
    assert get_val(fixture_dict, 'Name') == 'git'


def test_get_val_empty_dict():
    assert get_val({}, 'surname', 'Who is it?') == 'Who is it?'
    assert get_val({}, 'surname',) == 'git'
